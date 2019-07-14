from rest_framework import serializers
from . import models


class CustSerializer(serializers.ModelSerializer):
    class Meta:
        fields ='__all__'
        model = models.cust_info_model