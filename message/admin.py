from django.contrib import admin
from .models import Message, MessageToUser
from django.utils.html import format_html

# Register your models here. 

# class MessageAdminInline(admin.TabularInline):
#     model = Message
#     raw_id_fields = ['name', 'subject', 'email', 'body']


class MessageToUserAdminInline(admin.TabularInline):
    model = MessageToUser
    # list_display = ('message_id', 'title', 'body', 'other_email')
    

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'choise')
    readonly_fields = ('name','subject', 'email', 'body') # faqat o'qish un ishlatiladi
    search_fields = ('choise', 'status',)
    inlines = [MessageToUserAdminInline]

    # Function to change the icons (read - unread)
    def _(self, obj):
        if obj.CHOISE == 'Read':
            return True
        else:
            return False

    _.boolean = True

    # Function to color the text (read - unread)
    def status(self, obj):
        if obj.CHOISE == 'Read':
            color = '#80c904'
        else:
            color = 'red'
        return format_html('<strong><p> style="color:{}">{}</p></strong>'.format(color, obj.CHOISE))

    status.allow_tags = True

############
# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     raw_id_fields = ['product']

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'email',
#     'address', 'postal_code', 'city', 'paid',
#     'created', 'updated']

# list_filter = ['paid', 'created', 'updated']
# inlines = [OrderItemInline]