from django.db import models
from accounts.models import User
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    username= models.CharField(default='',max_length= 50)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length= 60)
    description = models.CharField(max_length= 250)
    posted_on = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default='')
    
    def __str__(self) -> str:
        return self.title
