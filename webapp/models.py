from django.db import models

# Create your models here.
class signupdb(models.Model):
    Signup_username=models.CharField(max_length=30,null=True,blank=True)
    Signup_email=models.EmailField(null=True,blank=True)
    Signup_mobile=models.IntegerField(null=True,blank=True)
    Signup_password=models.CharField(max_length=30,null=True,blank=True)
    Signup_confirm=models.CharField(max_length=30,null=True,blank=True)

class contactdb(models.Model):
    Contact_fullname=models.CharField(max_length=30,null=True,blank=True)
    Contact_email=models.EmailField(null=True,blank=True)
    Contact_subject=models.CharField(max_length=30,null=True,blank=True)
    Contact_message=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Contact_fullname

