from django.contrib import admin
from .models import Message
# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'reciever','message', 'is_read', 'time' ]
    list_editable = ['is_read']

admin.site.register(Message, MessageAdmin)