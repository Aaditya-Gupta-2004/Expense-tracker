from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=15)
    username = models.CharField(max_length=9)
    password = models.CharField(max_length=8)

    def  __str__(self):
        return self.username
    
class Exp(models.Model):
    categories_choices = [
        ("Food","Food"),
        ("Salary","Salary"),
        ("Utilities","Utilities"),
        ("Others","Others")
    ]

    Type_choices = [
        ("expense","expense"),
        ("credit","credit")
    ]
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)
    Amount = models.CharField(max_length=50)
    Type = models.CharField(choices=Type_choices,null=True,blank=True, max_length = 150)
    Category = models.CharField(choices=categories_choices,null=True,blank=True, max_length = 150)
    date = models.DateField(default=datetime.today)

    def  __str__(self):
        return self.Title