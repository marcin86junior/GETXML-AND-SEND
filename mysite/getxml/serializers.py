from rest_framework import serializers
from .models import books
from rest_framework import filters

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = books
        fields = '__all__'
