from django.db import models
from django.conf import settings

# Create your models here.
class Status(models.Model):
    #user= models.ForeignKey()
     #User= models.TextField(max_length=20,null=True,blank=True)
    Content=models.CharField(max_length=20,null=True,blank=True)
    User = models.CharField(max_length=20, null=False, blank=False)
    image=models.ImageField(upload_to="",blank=True,null=True)
    updated= models.DateTimeField(auto_now=True)
    TimeStamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.Content)[0:50]



class Musician(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    # change
    def __str__(self):
        return str(self.first_name)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Prajwalmodel(models.Model):
   # artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    skilss=models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    def __str__(self):
        return str(self.name)