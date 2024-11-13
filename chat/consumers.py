import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        # self.send(text_data=json.dumps({
        #     "type": "connection_established",
        #     "message": f"Connected to group {self.room_group_name}!"
        # }))

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        text_json = json.loads(text_data)
        message = text_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "message",
                "message": message
            }
        )

    def message(self, event):
        msg = event["message"]
        self.send(text_data=json.dumps({
            "type": "chat",
            "message": msg
        }))

    # def disconnect(self, code):
    #     pass
