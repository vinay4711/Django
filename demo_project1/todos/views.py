from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from . import models
from . import serializers
# Only get and Post- ADD NEW ONE
class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer

# VIEW, PUT , DELETE 
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer