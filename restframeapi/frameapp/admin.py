from django.contrib import admin
from .models import Status,Musician,Musician,Album,Prajwalmodel
from .model_one_one import Place,Waiter,Restaurant


class StatusAdmin(admin.ModelAdmin):
    list_display = ['User','Content','updated','TimeStamp']
admin.site.register(Status,StatusAdmin)

class MusicialAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','instrument']
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'release_date', 'num_stars','artist']
admin.site.register(Musician,MusicialAdmin)
admin.site.register(Album,AlbumAdmin)


class place_admin(admin.ModelAdmin):
    list_display = ['name', 'address']
admin.site.register(Place,place_admin)
class Restaurant_admin(admin.ModelAdmin):
    list_display = ['place', 'serves_hot_dogs','serves_pizza']
admin.site.register(Restaurant,Restaurant_admin)
class Waiter_admin(admin.ModelAdmin):
    list_display = ['restaurant', 'name']
admin.site.register(Waiter,Waiter_admin)


class Prajwal_admin(admin.ModelAdmin):
    list_display = ['id', 'name','skilss']
admin.site.register(Prajwalmodel,Prajwal_admin)

