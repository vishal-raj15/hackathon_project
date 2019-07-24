from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model): #how calss works in python
    name = models.CharField(max_length=50,default="")

    amount = models.CharField(max_length=50,default="")

    phone = models.CharField( max_length=10,default="")
    
    date=models.DateTimeField(auto_now_add=True , auto_now=False)

    def __str__(self):
        return (self.name,self.amount,self.phone ,self.date)
        



