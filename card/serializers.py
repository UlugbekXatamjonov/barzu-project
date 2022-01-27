from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'id', 
            'title', 
            'slug',
            'body',
            'image',
            'author',
            'status',
            'created',
        )
