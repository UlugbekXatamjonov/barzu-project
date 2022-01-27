from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

# Create your views here.

class MessageFormView(request):
    if request.method == 'POST':
        contact = Contact()
        fullname.request.POST.get('fullname')
        email.request.POST.get('email')
        subject.request.POST.get('subject')
        body.request.POST.get('body')
        created.request.POST.get('created')
        contact.fullname = fullname
        contact.email = email
        contact.subject = subject
        contact.body = body
        contact.created = created
        contact.save()
        # return HttpResponse("<h1> Thanks for contact us </h1>")

    # return render(request, 'messages.html')

