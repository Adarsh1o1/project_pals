from django.db import models
from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class ChatRoom(models.Model):
    name = models.CharField(max_length=255,) 
    sender = models.ForeignKey(User, related_name='sender_chat_rooms', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver_chat_rooms', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.CharField(max_length=10000, default='')
    is_read = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    chat_room = models.ForeignKey(ChatRoom, default='', related_name='messages', on_delete=models.CASCADE)
    class Meta:
        ordering = ['time']
        verbose_name = "Message"

    def __str__(self) -> str:
        return f'{self.sender}'
    