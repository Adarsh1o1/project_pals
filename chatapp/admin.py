from django.contrib import admin
from .models import *
# Register your models here.

class chatAdmin(admin.ModelAdmin):
    list_display = ['id','created_at']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['chat', 'sender','text', 'is_read', 'timestamp' ]
    list_editable = ['is_read']

admin.site.register(Chat, chatAdmin)
admin.site.register(Message, MessageAdmin)