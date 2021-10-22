from rest_framework import serializers
from django import forms
class User_Item(serializers.Serializer):
    name = serializers.CharField(max_length=70)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=20)
