from rest_framework import serializers
from .models import advetiser, ad, click, view

class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = advetiser
        fields = ['id', 'name']

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad
        fields = ['id', 'title', 'image', 'link', 'advertiser', 'approve']

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = click
        fields = ['id', 'ad', 'created_on', 'user_ip']

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = view
        fields = ['id', 'ad', 'created_on', 'user_ip']
