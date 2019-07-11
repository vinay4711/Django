from __future__ import unicode_literals
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    Email_Id = models.CharField(max_length=30)

    class Meta:
        db_table = "student"


class Mobile(models.Model):
    ModelName = models.CharField(max_length=20)
    Version = models.CharField(max_length=30)
    price = models.FloatField()

    class Meta:
        db_table = "Mobile"

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"

