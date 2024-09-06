from .models import *
from .models import Post
from rest_framework import serializers

class Post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','category','description'] 
    def validate(self, attrs):
        user = self.context.get('user')
        username= self.context.get('username')
        title = attrs.get('title')
        description = attrs.get('description')
        category = attrs.get('category')
        
        Post.objects.create(username=username, title = title, description = description, category = category, email= user.email)
        
        return attrs

class User_Post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['username','id','title','category','description','posted_on', 'email'] 