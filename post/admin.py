from django.contrib import admin
from .models import  Post
from django.utils.html import mark_safe
from parler.admin import TranslatableAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ('title', 'slug', 'author', 'created','status',"avatar_tag")
    list_filter = ('status', 'created',  'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ('status', 'created')
    readonly_fields = ('avatar_tag',)

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}
