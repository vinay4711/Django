from django.db import models

# Create your models here.

class Company(models.Model):
    C_Name=models.CharField(max_length=30)
    C_Class= models.CharField(max_length=10)
    C_Age=models.IntegerField()
    C_Addr= models.TextField(max_length=100)
