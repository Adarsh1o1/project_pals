import json
from channels.generic.websocket import AsyncWebsocketConsumer
from jwt.exceptions import InvalidTokenError
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from accounts.models import User,Profile
from asgiref.sync import sync_to_async

class testConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        token_key = self.scope['query_string'].decode().split("=")[1]
        user0 = await self.get_user(token_key)
        if not user0:
            await self.close()
        else:
            self.user0 = user0
            user1 = self.scope["url_route"]["kwargs"]["userId"]
            user_ids=sorted([int(user0.id),int(user1)])
            self.room_group_name = f"chat_{user_ids[0]}--{user_ids[1]}"
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json['username']
        #Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, 'username':username}
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message,'username':username}))

    @database_sync_to_async
    def get_user(self, token_key):
        try:
            access_token = AccessToken(token_key)
            userId = access_token.payload.get('user_id')
            user = User.objects.get(id=userId)
            self.username = user.username
            # print(user.username)
            return user
        except (InvalidTokenError, KeyError):
            return AnonymousUser()


class OnlineStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name='user'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
    
    async def receive(self, text_data=None, bytes_data=None):
        data=json.loads(text_data)
        username=data['username']
        user= await sync_to_async(User.objects.get)(username=username)
        online_status=data['online_status']
        # print(username, online_status)
        await self.ChangeOnlineStatus(user,online_status)

    async def disconnect(self, message):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def ChangeOnlineStatus(self, user, online_status):
        user=Profile.objects.get(user=user)
        if online_status==True:
            user.online_status = True
            user.save()
        else:
            user.online_status=False
            user.save()