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
from .serializers import chatSerializer


class chatHistory(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]
    def get(self, request):
        chats= list(chatModel.objects.filter(thread_name = 'chat_1--3'))
        serializer=chatSerializer(chats, many = True)
        return Response({'status': status.HTTP_200_OK, 'payload':serializer.data})


