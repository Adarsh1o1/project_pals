from .models import *
from accounts.models import User,Profile
from rest_framework import serializers
from datetime import datetime
from django.utils import timezone

# class chatSerializer(serializers.ModelSerializer):
#     time=  serializers.SerializerMethodField()
#     class Meta:
#         model = chatModel
#         fields = ['sender', 'Message', 'thread_name', 'time','time']


#     def get_time(self, obj):
#         # Format the timestamp to a readable format
#         datetime_obj = timezone.localtime(obj.timestamp) 
#         return datetime_obj.strftime("%B %d, %Y %H:%M")
#     def get_time(self, obj):
#         # Format the timestamp to a readable format
#         datetime_obj = timezone.localtime(obj.timestamp) 
#         return datetime_obj.strftime("%d/%m/%y %I:%M %p")


class chatSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()

    def get_date(self, obj):
        # Ensure the timestamp is in the correct timezone (IST)
        timestamp = timezone.localtime(obj.timestamp)
        # Convert to the desired date format: dd/mm/yy
        return timestamp.strftime("%d/%m/%y")

    def get_time(self, obj):
        # Ensure the timestamp is in the correct timezone (IST)
        timestamp = timezone.localtime(obj.timestamp)
        # Convert to the desired time format: %I:%M %p
        return timestamp.strftime("%I:%M %p")

    class Meta:
        model = chatModel
        fields = ['sender', 'Message', 'thread_name', 'date', 'time']


class ChatRequestSerializer(serializers.ModelSerializer):
    time=serializers.SerializerMethodField()
    class Meta:
        model= ChatRequest
        fields= "__all__"
    
    def time(self, obj):
        now = timezone.now()
        duration = now - obj.created_at
        if duration.days >= 1:
                return f"{duration.days} days ago"
        hours = duration.seconds // 3600
        return f"{hours} hours ago"