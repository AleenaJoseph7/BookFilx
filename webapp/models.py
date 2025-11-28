from django.db import models


# Create your models here.
class signupdb(models.Model):
    Signup_username = models.CharField(max_length=30, null=True, blank=True)
    Signup_email = models.EmailField(null=True, blank=True)
    Signup_mobile = models.IntegerField(null=True, blank=True)
    Signup_password = models.CharField(max_length=30, null=True, blank=True)
    Signup_confirm = models.CharField(max_length=30, null=True, blank=True)


class contactdb(models.Model):
    Contact_fullname = models.CharField(max_length=30, null=True, blank=True)
    Contact_email = models.EmailField(null=True, blank=True)
    Contact_subject = models.CharField(max_length=30, null=True, blank=True)
    Contact_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Contact_fullname


class cartdb(models.Model):
    Singlebook_username = models.CharField(max_length=30, null=True, blank=True)
    Singlebook_title = models.CharField(max_length=30, null=True, blank=True)
    Singlebook_price = models.IntegerField(null=True, blank=True)
    Singlebook_quantity = models.CharField(max_length=30, null=True, blank=True)
    Singlebook_total = models.IntegerField(null=True, blank=True)
    Singlebook_image = models.ImageField(upload_to="Cart Images", null=True, blank=True)

    def __str__(self):
        return self.Singlebook_title
