from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import CreateView, TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import *


# Create your views here.

class MessageView(CreateView):
    template_name = "contact.html"
    form_class =  MessageForm

    def get_success_url(self):
        return ('done') 


def done_page(request):
    return render(request, 'done_message.html', locals())
  

# ---------------New view-------------------- 

class Message_View(APIView):
    
    serializer_class = MessageSerializer
  
    def get(self, request):
        detail = [ {"name": detail.name,
                    "subject": detail.subject,
                    "email":detail.email,
                    "body":detail.body
                    }

        for detail in Message.objects.all()]
        return Response(detail)
  
    def post(self, request):
  
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)

