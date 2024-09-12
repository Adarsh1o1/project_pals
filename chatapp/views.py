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


class chatHistory(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]
    def list(self, request, *args, **kwargs):
        userid0= int(request.user.id)
        userid1 =int(self.kwargs['userid'])
        # if userid0 > userid1:
        #     thread_name = f'chat_{userid0}--{userid1}'
        # else:
        #     thread_name = f'chat_{userid1}--{userid0}'
        thread_name= sorted([int(userid0),int(userid1)])
        thread_name= f"chat_{thread_name[0]}--{thread_name[1]}"
        print(thread_name)
        chats= list(chatModel.objects.filter(thread_name = thread_name))
        serializer=chatSerializer(chats, many = True)
        return Response({'status': status.HTTP_200_OK, 'payload':serializer.data})

    # user_obj = User.objects.get(username=username)
    # users = User.objects.exclude(username=request.user.username)


    # message_objs = chatModel.objects.filter(thread_name=thread_name)