from django.db import models
from django.contrib.auth.models import AbstractUser,User
from datetime import date

# Create your models here.

class Gallary(models.Model):
	img =models.ImageField(upload_to='pics')

class User(AbstractUser):
	Name=models.CharField(null='True',max_length=30)
	email=models.EmailField(null='True')
	phno=models.CharField(null='True',max_length=30)
	address=models.TextField(null='True')
	city=models.CharField(max_length=30,null='True')
	state=models.CharField(max_length=40,null='True')
	pin=models.IntegerField(null='True')