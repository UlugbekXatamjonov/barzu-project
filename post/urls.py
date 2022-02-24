from django.urls import path
from .views import *
from django.utils.translation import gettext_lazy as _

app_name = "post"

# urlpatterns = [
#     # path(_('news/'), post_list, name= 'post_list'),
#     # path(_('<int:year>/<int:month>/<int:day>/<int:pk>'), post_detail, name="post_detail"),
#     # path(_('card/'), card_detail, name="card_detail"),
#     # path(_('about/'), Aboutpage, name='about'),
#     # # path(_('contact/'), Contactpage, name='contact'),
#     # path(_(''), Homepage, name="index"),
# ]



urlpatterns = [
    path(_('<int:year>/<int:month>/<int:day>/<int:pk>'), PostDetail, name="post_detail"),
    path(_('homepost/'), PostList_home.as_view(), name='home_post'),
    path(_(''), PostList.as_view(), name="post_list"),
]

# urlpatterns = [
#     path(_('<int:year>/<int:month>/<int:day>/<int:pk>'), card_detail, name="card_detail"),
# ]
