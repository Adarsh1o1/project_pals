from django.db import models
from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class Chat(models.Model):
    participants = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat between {self.participants.all()}"

    
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages', default='000')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    class Meta:
        ordering = ['timestamp']


    def __str__(self):
        return f"'{self.text}' from {self.sender} in chat {self.chat}"
    