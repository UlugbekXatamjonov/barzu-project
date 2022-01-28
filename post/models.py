from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import mark_safe
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.

STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    )

class Post(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("title"), max_length=200, db_index=True),
        slug = models.SlugField(_("slug"), max_length=250, unique=True, db_index=True),
        body = models.TextField(_("body"), db_index=True),
        tags = TaggableManager(_('tags')), # Tag maneger
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to="post_images/%Y/%m/%d/")
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') 
    views = models.PositiveIntegerField(default=0)

    class Meta: 
        # ordering = ('-created',)
        verbose_name = 'post'
        verbose_name_plural = 'posts' 

    def __str__(self): 
        return self.title

    def get_absolute_url(self):
        return reverse('postes:detail_post',
                       args=[self.created.year,
                             self.created.month,
                             self.created.day,
                             self.slug])

    def avatar_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
  
    avatar_tag.short_description = 'Rasmi'

    def __unicode__(self): 
        return self.title
