from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=25)
    first_name=models.CharField(max_length=25,null=True,blank=True)
    last_name=models.CharField(max_length=25,null=True,blank=True)
    email=models.EmailField()
    password=models.CharField(max_length=25)
    passwordconfirmation=models.CharField(max_length=25)

class Login(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)