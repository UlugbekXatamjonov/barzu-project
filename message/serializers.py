from rest_framework import serializers
from . models import *
  
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message()
        fields = ['name', 'subject', 'email', 'body']
