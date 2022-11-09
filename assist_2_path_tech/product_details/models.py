from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class User(models.Model):
    Product_Name = models.CharField(max_length=50)
    Price = models.IntegerField(null= True)
    Quantity = models.IntegerField(null = True)

