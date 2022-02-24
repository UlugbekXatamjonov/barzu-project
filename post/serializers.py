from rest_framework import serializers
from .models import Post
from taggit.serializers import (TagListSerializerField, TaggitSerializer)


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 
            'title',
            'body',
            'slug',
            'author',
            'image',
            'created',
            'views',
            )

