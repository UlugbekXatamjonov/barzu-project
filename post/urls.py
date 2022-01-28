from django.urls import path
from .views import ListPost, DetailPost
from django.utils.translation import gettext_lazy as _

app_name = "post"

urlpatterns = [
    path(_('<int:pk>/post/'), DetailPost.as_view(), name="detail_post"),
    path(_(''), ListPost.as_view(), name="list_post"),
]

