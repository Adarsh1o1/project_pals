from django.db import models
from accounts.models import User
# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')
    message = models.CharField(max_length=10000)
    is_read = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
     
    class Meta:
        ordering = ['time']
        verbose_name = "Message"

    def __str__(self) -> str:
        return f'{self.sender}'
    