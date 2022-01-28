from rest_framework import serializers
from .models import Post
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class PostSerializer(serializers.ModelSerializer, TaggitSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Post
        fields = (
            'id', 
            'title', 
            'slug',
            'author',
            'image',
            'body',
            'status',
            'created',
            'views',
            'tags',
        )

