from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate,login
from rest_framework import status,permissions
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .renderers import UserRenderer        
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework import generics
from django.db.models import Q
from django.contrib.auth.models import AnonymousUser
from .models import * 
# Create your views here.


class chatRoom(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]
    def post(self, request, ):
        data = request.data.get('receiver')
        username2 = get_object_or_404(User,username=data)
        username1 = request.user
        print(username2)
        chatRoom.name = f"{username1} and {username2}'s room"
        existing_chat_room = ChatRoom.objects.filter(name=chatRoom.name)
        if existing_chat_room:
            return JsonResponse({'room_name':chatRoom.name }, status=200)
        else:
            ChatRoom.objects.create(name = chatRoom.name, sender = username1, receiver= username2)
        return Response(status=status.HTTP_200_OK)