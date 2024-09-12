from .models import *
from accounts.models import User,Profile
from rest_framework import serializers
from datetime import datetime
from django.utils import timezone

class chatSerializer(serializers.ModelSerializer):
    time=  serializers.SerializerMethodField()
    class Meta:
        model = chatModel
        fields = ['sender', 'Message', 'thread_name', 'time']


    def get_time(self, obj):
        # Format the timestamp to a readable format
        datetime_obj = timezone.localtime(obj.timestamp) 
        return datetime_obj.strftime("%B %d, %Y %H:%M:%S")