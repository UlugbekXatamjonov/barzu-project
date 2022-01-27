from django.urls import path
from .views import ListCard, DetailCard

app_name = "card"

urlpatterns = [
    path('<int:pk>/card/', DetailCard.as_view(), name="detail_card"),
    path('', ListCard.as_view(), name="list_card"),
]
