from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


# Create your models here.

STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    )

class Card(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("title"), max_length=50, db_index=True),
        slug = models.SlugField(_("slug"), max_length=250, unique=True, db_index=True),
        body = models.CharField(_("body"), max_length=200, db_index=True),
    )
    image = models.ImageField(upload_to="card_image/%Y/%m/%d/", verbose_name="Foto surat")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card_posts', verbose_name="Muallif")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'card'
        verbose_name_plural = 'cards'

    def __str__(self): 
        return self.title

    def get_absolute_url(self):
        return reverse('card:card_detail',
                       args=[self.created.year,
                             self.created.month,
                             self.created.day,
                             self.pk])
                        
    def card_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))

    card_tag.short_description = 'Rasmi'

    def __unicode__(self): 
        return self.title

