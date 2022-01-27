from django.contrib import admin
from .models import  Card
from django.utils.html import mark_safe

# Register your models here.

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created','status',"card_tag")
    list_filter = ('status', 'created',  'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ('status', 'created')
    readonly_fields = ('card_tag',)

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

    def card_tag(self, obj):
        return obj.card_tag

    card_tag.short_description = 'Rasmi'