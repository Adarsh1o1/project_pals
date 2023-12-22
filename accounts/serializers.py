from .models import *
from .models import User,Profile
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ['email','username', 'password', 'password2','otp','first_name','last_name']
        extra_kwargs ={
            'password': {
                'write_only':True
            }
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('passwords did not match')
        
        if not attrs.get('username'):
            raise serializers.ValidationError("field username is required")
        
        if not attrs.get('first_name'):
            raise serializers.ValidationError("field first name is required")
        
        if not attrs.get('last_name'):
            raise serializers.ValidationError("field last name is required")
        
        return attrs           

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    class Meta:
        model = User
        fields = ['email', 'password']

        
class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(style= {'input_type':'password'},write_only = True, validators=[validate_password])
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True, validators=[validate_password])
    class Meta:
        fields = ['password','password2']
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError('passwords did not match')
        user.set_password(password)
        user.save()
        return attrs
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["full_name", "bio","verified","image"]
    