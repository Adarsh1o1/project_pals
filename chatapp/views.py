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
from .serializers import chatSerializer,ChatRequestSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# @method_decorator(csrf_exempt, name='dispatch')
# class Request(APIView):
#     permission_classes = [IsAuthenticated]
#     renderer_classes = [UserRenderer]
    
#     def post(self, request):
#         # Create a chat request
#         from_user = request.user
#         to_user = User.objects.get(username=request.data['to_user'])
#         # Check if there's already a request
#         if ChatRequest.objects.filter(from_user=from_user, to_user=to_user, status='pending').exists():
#             req=ChatRequest.objects.filter(from_user=from_user, to_user=to_user, status='pending')
#             print(req.status)
#             return Response({'detail': f'Request already {req.status}.'}, status=status.HTTP_400_BAD_REQUEST)
        # Create new chat request
        # chat_request = ChatRequest(from_user=from_user, to_user=to_user)
        # chat_request.save()
        # return Response({"id": chat_request.id,'detail': 'Chat request sent.'}, status=status.HTTP_201_CREATED)
        
class Request(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def post(self, request):
        # Create a chat request
        from_user = request.user
        to_user = User.objects.get(username=request.data['to_user'])

        # Check if there's already a request
        existing_request = ChatRequest.objects.filter(from_user=from_user, to_user=to_user, status='pending').first()
        
        if existing_request:
            return Response({'detail': f'Request already {existing_request.status}.'}, status=status.HTTP_400_BAD_REQUEST)

        # If no request exists, create a new one
        new_request = ChatRequest.objects.create(from_user=from_user, to_user=to_user)
        return Response({'detail': 'Chat request sent successfully.'}, status=status.HTTP_201_CREATED)

        

    
    def get(self, request, pk,action):
        # Accept or decline the request
        print(pk,action)
        chat_request = ChatRequest.objects.get(id=pk, to_user=request.user)
        if chat_request:
            if action == 'accept':
                chat_request.status = 'accepted'
                chat_request.save()
                return Response({'detail': 'Chat request accepted.'}, status=status.HTTP_200_OK)
            elif action == 'decline':
                chat_request.status = 'declined'
                chat_request.save()
                return Response({'detail': 'Chat request declined.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid action.'}, status=status.HTTP_400_BAD_REQUEST)

class PendingRequestsView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def get(self, request):
        # Get pending requests where the current user is the receiver
        pending_requests = ChatRequest.objects.filter(to_user=request.user, status='pending')
        serializer = ChatRequestSerializer(pending_requests, many=True)
        return Response(serializer.data)





class chatHistory(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]
    def list(self, request, *args, **kwargs):
        userid0= int(request.user.id)
        userid1 =int(self.kwargs['userid'])
        thread_name= sorted([int(userid0),int(userid1)])
        thread_name= f"chat_{thread_name[0]}--{thread_name[1]}"
        print(thread_name)
        chats= list(chatModel.objects.filter(thread_name = thread_name))
        serializer=chatSerializer(chats, many = True)
        return Response([serializer.data])
