from django.contrib import admin
from .models import *
# Register your models here.

class chatRoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'sender','receiver']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'reciever','message', 'is_read', 'time' ]
    list_editable = ['is_read']

admin.site.register(Message, MessageAdmin)
admin.site.register(ChatRoom, chatRoomAdmin)