from django.shortcuts import render

# api/views.py
from rest_framework import viewsets

from . import models
from . import serializers


class custViewSet(viewsets.ModelViewSet):
    queryset = models.cust_info_model.objects.all()

    serializer_class = serializers.CustSerializer