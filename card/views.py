from django.shortcuts import render, get_object_or_404
from .models import Card
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CardSerializers

# Create your views here.
# def card_detail(request):
#     cards = Card.objects.filter(status='published').all()
#     return render(request, 'galery.html', locals())


class CardList(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializers

class CardDetail(RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializers



