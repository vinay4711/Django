from rest_framework import serializers
from .model_one_one import Place,Restaurant,Waiter
from .models import Status
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['name', 'address']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant

class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
class Status_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields=['Content','User']

from .models import *
from rest_framework import serializers, fields


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date', 'num_stars')


class MusicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument')