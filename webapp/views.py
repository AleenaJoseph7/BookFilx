from django.shortcuts import render, redirect
from Myapp.models import catergorydb, bookdb
from webapp.models import signupdb, contactdb, cartdb


# Create your views here.
def Homepage(request):
    books = bookdb.objects.all()
    category = catergorydb.objects.all()
    return render(request, "Homepage.html", {'category': category, 'books': books})


def Aboutpage(request):
    category = catergorydb.objects.all()
    return render(request, "aboutpage.html", {'category': category})


def Contactpage(request):
    category = catergorydb.objects.all()
    return render(request, "contact.html", {'category': category})


def Popularpage(request):
    books = bookdb.objects.all()
    category = catergorydb.objects.all()
    return render(request, "popular.html", {'category': category, 'books': books})


def Checkoutpage(request):
    category = catergorydb.objects.all()
    return render(request, "checkoutpage.html", {'category': category})


def Filterbooks(request, category_name):
    category = catergorydb.objects.all()
    books = bookdb.objects.filter(Book_category=category_name)
    return render(request, "Filter_books.html", {'category': category, 'books': books, 'category_name': category_name})


def Singlebook(request, book_id):
    category = catergorydb.objects.all()
    books = bookdb.objects.get(id=book_id)
    return render(request, "singlebook.html", {'books': books, 'category': category, })


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

        return redirect(Contactpage)


def Cartpage(request):
    cart = cartdb.objects.all()
    return render(request, "Cartpage.html", {'cart': cart})


def Usersigninpage(request):
    return render(request, "Usersigninpage.html")


def Usersignuppage(request):
    return render(request, "Usersignuppage.html")


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
            # alert message
            return redirect(Usersignuppage)
        elif signupdb.objects.filter(Signup_email=signup_email).exists():
            # alert message
            return redirect(Usersignuppage)
        elif signupdb.objects.filter(Signup_mobile=signup_mobile).exists():
            return redirect(Usersignuppage)
        else:
            ob.save()
            return redirect(Usersigninpage)


def login(request):
    if request.method == 'POST':
        signin_username = request.POST.get('signin_username')
        signin_password = request.POST.get('signin_password')

        if signupdb.objects.filter(Signup_username=signin_username, Signup_password=signin_password).exists():
            request.session['username'] = signin_username
            request.session['password'] = signin_password
            return redirect(Homepage)

        else:
            return redirect(Usersigninpage)

    else:
        return redirect(Usersigninpage)


def logout(request):
    del request.session['username']
    del request.session['password']

    return redirect(Usersigninpage)
