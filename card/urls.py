from django.urls import path
from .views import *
from django.utils.translation import gettext_lazy as _

app_name = "card"

# urlpatterns = [
#     path(_('<int:year>/<int:month>/<int:day>/<int:pk>'), card_detail, name="card_detail"),
# ]


urlpatterns = [
    path(_('<int:year>/<int:month>/<int:day>/<int:pk>'),CardDetail.as_view()),
    path(_(''),CardList.as_view()),
]

