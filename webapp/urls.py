from django.urls import path
from webapp import views

urlpatterns=[
    path('Homepage/',views.Homepage,name="Homepage"),
    path('AboutPage/',views.Aboutpage,name="Aboutpage"),
    path('Contactpage/',views.Contactpage,name="Contactpage"),
    path('Popularpage/',views.Popularpage,name="Popularpage"),
    path('Checkoutpage/',views.Checkoutpage,name="Checkoutpage"),
    path('Filterbooks/<category_name>/',views.Filterbooks,name="Filterbooks"),
    path('Singlebook/<int:book_id>/',views.Singlebook,name="Singlebook"),
    path('savecontact/',views.savecontact,name="savecontact"),

    path('Usersigninpage/',views.Usersigninpage,name="Usersigninpage"),
    path('Usersignuppage/',views.Usersignuppage,name="Usersignuppage"),
    path('Saveusersignup/',views.Saveusersignup,name="Saveusersignup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
]