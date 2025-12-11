from os import remove

from django.shortcuts import render, redirect
from Myapp.models import catergorydb, bookdb
from webapp.models import contactdb,Checkoutdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.contrib import messages


# Create your views here.
def index(request):
    mcount = contactdb.objects.count()
    date = datetime.datetime.now()
    book_count = bookdb.objects.count()
    category_count = catergorydb.objects.count()
    return render(request, "index.html", {'book_count': book_count,
                                          'category_count': category_count,
                                          'date': date, 'mcount': mcount})


def addcatergory(request):
    date = datetime.datetime.now()
    return render(request, "add_catergory.html", {'date': date})


def savecatergory(request):
    if request.method == 'POST':
        catergory_name = request.POST.get('catergory_name')
        catergory_description = request.POST.get('catergory_description')
        catergory_cover = request.FILES.get('catergory_cover')

        ob = catergorydb(Catergory_name=catergory_name,
                         Catergory_description=catergory_description,
                         Catergory_cover=catergory_cover)
        ob.save()
        messages.success(request, "Catergory Saved Succesfully!")
        return redirect(addcatergory)


def displaycatergory(request):
    date = datetime.datetime.now()
    data = catergorydb.objects.all()
    return render(request, "displaycatergory.html", {'data': data, 'date': date})


def editcatergory(request, c_id):
    date = datetime.datetime.now()
    catergory = catergorydb.objects.get(id=c_id)
    return render(request, "edit_catergory.html", {'catergory': catergory, 'date': date})


def updatecatergory(request, c_id):
    if request.method == 'POST':
        catergory_name = request.POST.get('catergory_name')
        catergory_description = request.POST.get('catergory_description')
        try:
            catergory_cover = request.FILES['catergory_cover']
            fs = FileSystemStorage()
            files = fs.save(catergory_cover.name, catergory_cover)
        except MultiValueDictKeyError:
            files = catergorydb.objects.get(id=c_id).Catergory_cover

        catergorydb.objects.filter(id=c_id).update(Catergory_name=catergory_name,
                                                   Catergory_description=catergory_description,
                                                   Catergory_cover=files)
        messages.success(request, "Catergory Updated Successfully !")
        return redirect(displaycatergory)


def deletecatergory(request, c_id):
    data = catergorydb.objects.filter(id=c_id)
    data.delete()
    messages.warning(request, "Catergory Deleted Successfully !")
    return redirect(displaycatergory)


def addbook(request):
    date = datetime.datetime.now()
    category = catergorydb.objects.all()
    return render(request, "add_book.html", {'category': category, 'date': date})


def savebook(request):
    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        book_author = request.POST.get('book_author')
        book_category = request.POST.get('book_category')
        book_price = request.POST.get('book_price')
        book_publisher = request.POST.get('book_publisher')
        book_description = request.POST.get('book_description')
        book_cover = request.FILES.get('book_cover')

        ob = bookdb(Book_title=book_title,
                    Book_author=book_author,
                    Book_category=book_category,
                    Book_price=book_price,
                    Book_publisher=book_publisher,
                    Book_description=book_description,
                    Book_cover=book_cover)
        ob.save()
        messages.success(request, "Book Added Successfully !")
        return redirect(addbook)


def displaybook(request):
    date = datetime.datetime.now()
    data = bookdb.objects.all()
    return render(request, "display_book.html", {'data': data, 'date': date})


def editbook(request, b_id):
    date = datetime.datetime.now()
    book = bookdb.objects.get(id=b_id)
    category = catergorydb.objects.all()
    return render(request, "edit_book.html", {'book': book, 'category': category, 'date': date})


def updatebook(request, b_id):
    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        book_author = request.POST.get('book_author')
        book_category = request.POST.get('book_category')
        book_price = request.POST.get('book_price')
        book_publisher = request.POST.get('book_publisher')
        book_description = request.POST.get('book_description')
        try:
            book_cover = request.FILES['book_cover']
            fs = FileSystemStorage()
            files = fs.save(book_cover.name, book_cover)
        except MultiValueDictKeyError:
            files = bookdb.objects.get(id=b_id).Book_cover

        bookdb.objects.filter(id=b_id).update(Book_title=book_title,
                                              Book_author=book_author,
                                              Book_category=book_category,
                                              Book_price=book_price,
                                              Book_publisher=book_publisher,
                                              Book_description=book_description,
                                              Book_cover=files)
        messages.success(request, "Book Updated Successfully !")
        return redirect(displaybook)


def deletebook(request, b_id):
    data = bookdb.objects.filter(id=b_id)
    data.delete()
    messages.warning(request, "Book Deleted Succesfully !")
    return redirect(displaybook)


def displaymessage(request):
    data = contactdb.objects.all()
    return render(request, "display_messages.html", {'data': data})


def deletemessage(request, m_id):
    data = contactdb.objects.filter(id=m_id)
    data.delete()
    messages.warning(request, "Message Deleted Succesfully !")
    return redirect(displaymessage)

def Orderlist(request):
    date=datetime.datetime.now()
    data = Checkoutdb.objects.all().order_by('-id')
    return render(request, "Order.html", {'data': data,'date':date})


def Deleteorder(request, id):
    Checkoutdb.objects.filter(id=id).delete()
    return redirect('CheckoutList')


def adminloginpage(request):
    return render(request, "admin_login.html")


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username__contains=username).exists():
            data = authenticate(username=username, password=password)
            if data is not None:
                login(request, data)
                request.session['username'] = username
                msg=messages.success(request, "Admin Login Successful")
                return redirect(index)
            else:
                messages.error(request,"Incorrect Password or Username!")
                return redirect(adminloginpage)
        else:
            messages.error(request, "Username doesnt Exist!")
            return redirect(adminloginpage)


def adminlogout(request):
    del request.session['username']
    messages.success(request, "Admin Logout Successful")
    return redirect(adminloginpage)
