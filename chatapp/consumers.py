import json
from channels.generic.websocket import AsyncWebsocketConsumer
from jwt.exceptions import InvalidTokenError
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from accounts.models import User

class testConsumer(AsyncWebsocketConsumer):
    username = ''
    # async def connect(self):
        
    #     self.room_name = 'testing'
    #     self.room_group_name = f"chat_{self.room_name}"

    #     # Join room group
    #     await self.channel_layer.group_add(self.room_group_name, self.channel_name)

    #     await self.accept()
    async def connect(self):
        token_key = self.scope['query_string'].decode().split("=")[1]
        user = await self.get_user(token_key)
        if not user:
            await self.close()
        else:
            self.user = user
            self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
            self.room_group_name = f"chat_{self.room_name}"
            # Join room group
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json['username']
        print(username)
        #Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, 'username':username}
        )

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

