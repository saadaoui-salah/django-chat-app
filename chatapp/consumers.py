from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def chat_message(self, event):
        print("tester")
        tester = event['tester']
        await self.send(text_data=json.dumps({
            'tester': tester
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,    
        )
        
    # Receiving msg from the client
    async def receive(self, text_data):
        data_json = json.loads(text_data)
        message = data_json['message']
        username = data_json['username']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':"chat_message",
                'message':message,
                'username':username
            }
        )

    # send the message to the client
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message': message,
            'username':username,
            }))