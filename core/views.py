from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from rest_framework import status,permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .renderers import UserRenderer   
from .helpers import send_connect_mail   
import random 
from rest_framework import generics

@renderer_classes([UserRenderer])
@permission_classes([IsAuthenticated])
class create_post(APIView):
    def post(self, request):
        data = request.data
        user = request.user
        serializer = Post_serializer(data = data, context={'user':request.user,'username':request.user})
        if serializer.is_valid(raise_exception=True):
            print(user,data)
            return Response({"status":200,"msg": "Post created successfully"},status=status.HTTP_200_OK)
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST, 'msg': 'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        pass
    def put(self):
        pass
    def delete(self, request):
        pass

@renderer_classes([UserRenderer])
@permission_classes([IsAuthenticated])
class show_all_posts(APIView):
    def get(self, request):
        posts = list(Post.objects.all())
        random.shuffle(posts)
        random_posts = posts[:]
        serializer = User_Post_serializer(posts, many=True)
        return Response({'status': status.HTTP_200_OK, 'payload':serializer.data})

@renderer_classes([UserRenderer])
@permission_classes([IsAuthenticated])
class connect(APIView):
    def post(self, request):
        data = request.data
        initiater = User.objects.get(email = data.get('email'))
        if(send_connect_mail(initiater,request.user)):
            return Response({'status': status.HTTP_200_OK, "message": "mail sent successfully"})
        return Response({'status':status.HTTP_400_BAD_REQUEST, 'msg': 'something went wrong'},status=status.HTTP_400_BAD_REQUEST)    


class show_user_post(generics.ListAPIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    # queryset
    serializer_class = User_Post_serializer
    
    def get_queryset(self):
       return Post.objects.filter(user=self.request.user)