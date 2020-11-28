from django.db import models

# Create your models here.
class user(models.Model):
    userid=models.IntegerField(primary_key=True)

    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    gender = models.CharField(max_length=100)

class bussinesspage(models.Model):
    companyname = models.CharField(max_length=100)
    bid = models.IntegerField(primary_key=True)
    data = models.FileField()
    source = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contactno = models.IntegerField()
    rating = models.CharField(max_length=100)
    listed = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

