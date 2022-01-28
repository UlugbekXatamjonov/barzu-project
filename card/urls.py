from django.urls import path
from .views import ListCard, DetailCard
from django.utils.translation import gettext_lazy as _

app_name = "card"

urlpatterns = [
    path(_('<int:pk>/card/'), DetailCard.as_view(), name="detail_card"),
    path(_(''), ListCard.as_view(), name="list_card"),
]
