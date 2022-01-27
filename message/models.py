from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=70, verbose_name='Full name')
    subject = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    