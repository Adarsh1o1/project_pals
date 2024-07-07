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
        # print(username2)
        name = f"{username1}AND{username2}"
        ultaName = f"{username2}AND{username1}"
        existing_chat_room = ChatRoom.objects.filter(name=name) or ChatRoom.objects.filter(name=ultaName)
        if existing_chat_room:
            return JsonResponse({'room_name':name, 'sender':f'{username1}', 'receiver':f'{username2}'}, status=200)
        else:
            ChatRoom.objects.create(name = name, sender = username1, receiver= username2)
        return Response({'room_name':name, 'sender':f'{username1}', 'receiver':f'{username2}'},status=status.HTTP_200_OK)
    
    