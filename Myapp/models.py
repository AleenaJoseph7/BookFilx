from django.db import models

# Create your models here.
class catergorydb(models.Model):
    Catergory_name=models.CharField(max_length=40,null=True,blank=True)
    Catergory_description=models.TextField(null=True,blank=True)
    Catergory_cover=models.ImageField(upload_to="Catergory Cover Image",null=True,blank=True)


class bookdb(models.Model):
    Book_title=models.CharField(max_length=40,null=True,blank=True)
    Book_author=models.CharField(max_length=40,null=True,blank=True)
    Book_category=models.CharField(max_length=40,null=True,blank=True)
    Book_price=models.IntegerField(null=True,blank=True)
    Book_publisher=models.CharField(max_length=40,null=True,blank=True)
    Book_description=models.TextField(null=True,blank=True)
    Book_cover=models.ImageField(upload_to="Book Cover Images",null=True,blank=True)

