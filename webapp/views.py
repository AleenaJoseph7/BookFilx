from django.shortcuts import render, redirect
from Myapp.models import catergorydb, bookdb
from webapp.models import signupdb, contactdb, cartdb, Checkoutdb
from django.contrib import messages

import razorpay


# Create your views here.
def Homepage(request):
    books = bookdb.objects.all()
    category = catergorydb.objects.all()

    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = cartdb.objects.filter(Singlebook_username=uname).count()

    return render(request, "Homepage.html", {'category': category, 'books': books, 'cart_count': cart_count})


def Aboutpage(request):
    category = catergorydb.objects.all()

    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = cartdb.objects.filter(Singlebook_username=uname).count()

    return render(request, "aboutpage.html", {'category': category, 'cart_count': cart_count})


def Contactpage(request):
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = cartdb.objects.filter(Singlebook_username=uname).count()

    category = catergorydb.objects.all()
    return render(request, "contact.html", {'category': category, 'cart_count': cart_count})


def Popularpage(request):
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = cartdb.objects.filter(Singlebook_username=uname).count()

    books = bookdb.objects.all()
    category = catergorydb.objects.all()
    return render(request, "popular.html", {'category': category, 'books': books, 'cart_count': cart_count})


def Checkoutpage(request):
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = cartdb.objects.filter(Singlebook_username=uname).count()

    category = catergorydb.objects.all()

    cart = cartdb.objects.filter(Singlebook_username=request.session['username'])
    # receipt calculation
    sub_total = 0
    total_amount = 0
    delivery = 0
    gst = 0
    discount = 0
    for i in cart:
        sub_total += i.Singlebook_total
        if sub_total < 500:
            delivery = 50
        else:
            delivery = 0
        discount = round((sub_total * 0.10))
        gst = round((sub_total + delivery) * 0.05)
        total_amount = round(((sub_total + gst + delivery) - discount))

    return render(request, "checkoutpage.html", {'category': category, 'cart_count': cart_count,
                                                 'sub_total': sub_total,
                                                 'delivery': delivery,
                                                 'gst': gst,
                                                 'total_amount': total_amount,
                                                 'discount': discount,
                                                 'cart': cart
                                                 })


def Filterbooks(request, category_name):
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = cartdb.objects.filter(Singlebook_username=uname).count()

    category = catergorydb.objects.all()
    books = bookdb.objects.filter(Book_category=category_name)
    return render(request, "Filter_books.html",
                  {'category': category, 'books': books, 'category_name': category_name, 'cart_count': cart_count})


def Singlebook(request, book_id):
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = cartdb.objects.filter(Singlebook_username=uname).count()

    category = catergorydb.objects.all()
    books = bookdb.objects.get(id=book_id)
    return render(request, "singlebook.html", {'books': books, 'category': category, 'cart_count': cart_count})


def savecontact(request):
    if request.method == 'POST':
        contact_fullname = request.POST.get('contact_fullname')
        contact_email = request.POST.get('contact_email')
        contact_subject = request.POST.get('contact_subject')
        contact_message = request.POST.get('contact_message')

        ob = contactdb(Contact_fullname=contact_fullname, Contact_email=contact_email,
                       Contact_subject=contact_subject,
                       Contact_message=contact_message)

        ob.save()
        messages.success(request, "Feedback Added Succesfully!")
        return redirect(Contactpage)


def Cartpage(request):
    cart = cartdb.objects.filter(Singlebook_username=request.session['username'])
    category = catergorydb.objects.all()
    books = bookdb.objects.all()

    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = cartdb.objects.filter(Singlebook_username=uname).count()

    # receipt calculation
    sub_total = 0
    total_amount = 0
    delivery = 0
    gst = 0
    discount = 0
    for i in cart:
        sub_total += i.Singlebook_total
        if sub_total < 500:
            delivery = 50
        else:
            delivery = 0
        discount = round((sub_total * 0.10))
        gst = round((sub_total + delivery) * 0.05)
        total_amount = round(((sub_total + gst + delivery) - discount))

    return render(request, "Cartpage.html",
                  {'cart': cart,
                   'category': category,
                   'books': books,
                   'cart_count': cart_count,
                   'sub_total': sub_total,
                   'delivery': delivery,
                   'gst': gst,
                   'total_amount': total_amount,
                   'discount': discount})


def savecart(request):
    if request.method == 'POST':
        singlebook_quantity = request.POST.get('singlebook_quantity')
        singlebook_total = request.POST.get('singlebook_total')
        singlebook_title = request.POST.get('singlebook_title')
        singlebook_price = request.POST.get('singlebook_price')
        singlebook_username = request.POST.get('singlebook_username')
        book = bookdb.objects.filter(Book_title=singlebook_title).first()
        singlebook_image = book.Book_cover
        bookid = book.id

        ob = cartdb(Singlebook_username=singlebook_username,
                    Singlebook_title=singlebook_title,
                    Singlebook_price=singlebook_price,
                    Singlebook_quantity=singlebook_quantity,
                    Singlebook_total=singlebook_total,
                    Singlebook_image=singlebook_image,
                    Bookid=bookid)

        ob.save()
        messages.success(request, "Added to Cart !")
        return redirect(Homepage)


def deletecart(request, c_id):
    data = cartdb.objects.filter(id=c_id).delete()
    return redirect(Cartpage)


def savecheckout(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        total_amount = request.POST.get('total_amount')

        ob = Checkoutdb(Fullname=fullname,
                        Email=email,
                        Phone=phone,
                        Address=address,
                        Pincode=pincode,
                        Total_amount=total_amount)

        ob.save()
        messages.success(request,"Checkout Successfully!")
        return redirect(PaymentPage)

def PaymentPage(request):
    category = catergorydb.objects.all()

    uname = request.session.get('username')
    if uname:
        cart_count = cartdb.objects.filter(Singlebook_username=uname).count()

    #payment details
    customer=Checkoutdb.objects.order_by("-id").first()
    pay=customer.Total_amount
    amount=int(pay*100)
    pay_str=str(amount)

    if request.method=='POST':
        amount_currency='INR'
        client = razorpay.Client(auth=('rzp_test_0ib0jPwwZ7I1lT', 'VjHNO5zKeKxz8PYe7VnzwxMR'))
        payment=client.order.create({'amount':amount,'amount_currency':amount_currency})


    return render(request,"PaymentPage.html",
                  {'category':category,
                   'cart_count':cart_count,
                   'pay_str':pay_str,
                   })

def Usersigninpage(request):
    return render(request, "Usersigninpage.html")


def Usersignuppage(request):
    return render(request, "Usersignuppage.html")


def SignupDisplaypage(request):
    data = signupdb.objects.all()
    return render(request, "signupdbdisplay.html", {'data': data})


def DeleteSignup(request, user_id):
    user = signupdb.objects.get(id=user_id)
    user.delete()
    return redirect("SignupDisplaypage")


def Saveusersignup(request):
    if request.method == 'POST':
        signup_username = request.POST.get('signup_username')
        signup_email = request.POST.get('signup_email')
        signup_mobile = request.POST.get('signup_mobile')
        signup_password = request.POST.get('signup_password')
        signup_confirm = request.POST.get('signup_confirm')

        ob = signupdb(Signup_username=signup_username,
                      Signup_email=signup_email,
                      Signup_mobile=signup_mobile,
                      Signup_password=signup_password,
                      Signup_confirm=signup_confirm)

        if signupdb.objects.filter(Signup_username=signup_username).exists():
            messages.error(request, "Username Already Exists!")
            return redirect(Usersignuppage)
        elif signupdb.objects.filter(Signup_email=signup_email).exists():
            messages.error(request, "Email Already Exists!")
            return redirect(Usersignuppage)
        elif signupdb.objects.filter(Signup_mobile=signup_mobile).exists():
            messages.error(request, "Mobile Number Already Exists!")
            return redirect(Usersignuppage)
        else:
            ob.save()
            messages.success(request, "Sign up Successfull!")
            return redirect(Usersigninpage)


def login(request):
    if request.method == 'POST':
        signin_username = request.POST.get('signin_username')
        signin_password = request.POST.get('signin_password')

        if signupdb.objects.filter(Signup_username=signin_username, Signup_password=signin_password).exists():
            request.session['username'] = signin_username
            messages.success(request, "Login Successfull!")
            return redirect(Homepage)

        else:
            messages.error(request, "Username or Password  Incorrect!")
            return redirect(Usersigninpage)

    else:
        messages.error(request, "Tru Again !")
        return redirect(Usersigninpage)


def logout(request):
    del request.session['username']
    messages.success(request, "Logout Succesfull!")
    return redirect(Usersigninpage)
