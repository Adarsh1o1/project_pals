from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('chatHistory/', chatHistory.as_view() ),
]