from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CardSerializer
from .models import Card
# Create your views here.


class ListCard(ListAPIView):
    queryset = Card.objects.order_by('-created').all()
    serializer_class = CardSerializer


class DetailCard(RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer