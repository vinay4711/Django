from django.db import models

# Create your models here.

from django.db import models

class BookAuthor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class BookPublisher(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(BookAuthor)
    publisher = models.ForeignKey(BookPublisher, on_delete=models.CASCADE)
    #pubdate = models.DateField()
    def __str__(self):
        return self.name
class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return str("{}".format(self.name))