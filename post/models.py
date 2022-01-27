from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import mark_safe
from taggit.managers import TaggableManager




# Create your models here.

STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    )

class PublishedManager(models.Manager): 
    def get_queryset(self): 
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    title = models.CharField(max_length=200, )
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to="post_images/%Y/%m/%d/")
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') 
    views = models.PositiveIntegerField(default=0)
    # tags = models.CharField(max_length=70) # Tag maneger
    tags = TaggableManager() # Tag maneger
    objects = models.Manager() # The default manager. 
    published = PublishedManager() # Our custom manager.
# 
# date_of_birth = forms.DateField(input_formats=[TIME_FORMAT], label="Date of Birth", required=False, help_text="Format like 17.12.1979")
    
    class Meta: 
        ordering = ('-created',) 

    def __str__(self): 
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.created.year,
                             self.created.month,
                             self.created.day,
                             self.slug])

    def avatar_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
    
    avatar_tag.short_description = 'Rasmi'
