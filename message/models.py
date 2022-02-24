from django.db import models
from django.core.mail import send_mail

# Create your models here.

CHOISE = (
    ('Read', 'Read'),
    ('Unread', 'Unread'),
)

class Message(models.Model):
    name = models.CharField(max_length=70, verbose_name='Full name')
    subject = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    choise = models.CharField(max_length=50, null=True, choices=CHOISE, default='Unread', verbose_name='Habar holati')
    
    def __str__(self):
        return self.name


class MessageToUser(models.Model):
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='message_user')
    title = models.CharField(max_length=250)
    body = models.TextField()

    def save(self, *args, **kwargs):
        to = (self.message_id.email,)
        fromm = "info@uztexltd.uz"
        title = self.title
        body = self.body
        send_mail(title, body, fromm, to)
        super().save(*args, **kwargs)

