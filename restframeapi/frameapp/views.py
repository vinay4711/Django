from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from django.core.serializers import serialize
# Create your views here.
import json
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
class MusicianListView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()


class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class prajwalview(View):

    def get(self, request, *args, **kwargs):
        info = Prajwalmodel.objects.all()
        #empdata = {'eno': emp.eno, 'ename': emp.ename, 'esal': emp.esal, 'eaddr': emp.eaddr}
        data = serialize('json', info)
        #json_data = json.dumps(info)
        #return HttpResponse(json_data, content_type='application/json')
        #return JsonResponse(data)
        return HttpResponse(data,content_type='application/json')



