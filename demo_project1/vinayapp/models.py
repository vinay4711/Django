from django.db import models

# Create your models here.
class cust_info_model(models.Model):
    name=models.CharField(max_length=20,blank=False)
    mobile=models.IntegerField(max_length=10,blank=True)
    City=models.CharField(max_length=30)
    

