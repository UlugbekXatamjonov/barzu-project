from django.urls import path
from .views import *
from django.utils.translation import gettext_lazy as _


app_name = 'message'

urlpatterns = [
    path(_(''), MessageView.as_view(), name='message'),
    path(_('done/'), done_page, name='done_message'),
    path(_('messageform/'), Message_View.as_view(), name='messageform')
]
