from django.db import models

class Studnet(models.Model):
    S_Name=models.CharField(max_length=30)
    S_Class= models.TextField(max_length=10)
    s_Age=models.IntegerField(max_length=2)
    s_mobile= models.IntegerField(max_length=10)
