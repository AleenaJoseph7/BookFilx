from django.urls import path
from Myapp import views

urlpatterns=[
    path('Home/',views.index,name="Home"),

    path('addcatergory/',views.addcatergory,name="addcatergory"),
    path('savecatergory/',views.savecatergory,name="savecatergory"),
    path('editcatergory/<int:c_id>/',views.editcatergory,name="editcatergory"),
    path('updatecatergory/<int:c_id>/',views.updatecatergory,name="updatecatergory"),
    path('deletecatergory/<int:c_id>/',views.deletecatergory,name="deletecatergory"),

    path('addbook/',views.addbook,name="addbook"),
    path('savebook/', views.savebook, name="savebook"),
    path('editbook/<int:b_id>/', views.editbook, name="editbook"),
    path('updatebook/<int:b_id>/', views.updatebook, name="updatebook"),
    path('deletebook/<int:b_id>/', views.deletebook, name="deletebook"),
    path('displaybook/',views.displaybook,name="displaybook"),
    path('displaycatergory/',views.displaycatergory,name="displaycatergory"),

    path('displaymessage/',views.displaymessage,name="displaymessage"),
    path('deletemessage/<int:m_id>/',views.deletemessage,name="deletemessage"),

    path('adminloginpage/',views.adminloginpage,name="adminloginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout")



]