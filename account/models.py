import profile
from typing import Any
from django.db import models

# Create your models here.
class student(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    rollno = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    city=models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    profile = models.ImageField(upload_to="static/known")

class teacher(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    contanct = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    city=models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
