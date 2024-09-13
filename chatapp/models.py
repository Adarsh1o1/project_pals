from django.db import models
from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class ChatRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)



class chatModel(models.Model):
    sender = models.CharField(max_length=100, default=None)
    Message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    thread_name = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.Message
