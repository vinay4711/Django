from django.contrib import admin
from .models import Book,BookAuthor,BookPublisher,Store

class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ['name','age']
admin.site.register(BookAuthor,BookAuthorAdmin)




class BookPublisherAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(BookPublisher,BookPublisherAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['name','price','rating']
admin.site.register(Book,BookAdmin)

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Store,StoreAdmin)