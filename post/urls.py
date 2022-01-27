from django.urls import path
from .views import ListPost, DetailPost

app_name = "post"

urlpatterns = [
    path('', ListPost.as_view(), name="list_post"),
    path('<int:pk>/post/', DetailPost.as_view(), name="detail_post"),
]

