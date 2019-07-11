from django.conf import settings
from django.db import models
def upload_update_imgae(instance,filename):
    return "updates/{user}/{filename}".format(user=instance.user,filename=filename)

class update(models.Model):
    user= models.CharField(max_length=50,blank=True,null=True)
    content= models.TextField(blank=True,null=True)
    image= models.ImageField(upload_to=upload_update_imgae,blank=True,null=True)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content or ""


class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=60)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=200)
    def __str__(self):
        return self.ename or ""
