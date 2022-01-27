from rest_framework import serializers
from .models import Message
from taggit.serializers import (TagListSerializerField)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message()
        fields = (
          'name',
          'subject',
          'email',
          'body',
          'created',
        )

