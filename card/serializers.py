from rest_framework import serializers
from .models import Card


class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'id',
            'title',
            'body',
            'slug',
            'image',
            'author',
            'created',
            )

