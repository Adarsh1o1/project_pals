from django.contrib import admin
from .models import chatModel, ChatRequest
# Register your models here.

admin.site.register(chatModel)
admin.site.register(ChatRequest)