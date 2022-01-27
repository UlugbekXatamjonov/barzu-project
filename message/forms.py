from django.forms import ModelForm
from .models import Message

class MessageForm(ModelForm):
    model = Message
    fields = ('name', 'subject', 'email', 'body', 'created')
    



