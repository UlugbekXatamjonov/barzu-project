from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import mark_safe

# Create your models here.

STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    )

class Card(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.CharField(max_length=200)
    image = models.ImageField(upload_to="card_image/%Y/%m/%d/", verbose_name="Foto surat")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card_posts', verbose_name="Muallif")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ('-created',) 

    def __str__(self): 
        return self.title

    def get_absolute_url(self):
        return reverse('posts:card_detail',
                       args=[self.created.year,
                             self.created.month,
                             self.created.day,
                             self.slug])
                        
    def card_tag(self):
        return mark_safe('<img src="media/%s" width="50" height="50" />' % (self.image))

    card_tag.short_description = 'Rasmi'
