from rest_framework import serializers
from .models import Question
#serializers.Serializer if we want to write all the field name
#serializers.ModelSerializer - if u have already created the model , then create the model searlizer

#serializers.HyperlinkedModelSerializer
class Questionserializers(serializers.ModelSerializer):
    class meta:
        model=Question
        fields=['question_text','quest_Type']