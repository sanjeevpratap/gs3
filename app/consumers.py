
#Chat app with static group name
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket Connected... ',event)
        print('ssssChannel layer.. ', self.channel_layer)    #get default channel layer from a project
        print('Channel name.. ', self.channel_name)    #get default channel name from a project
        
        self.group_name=self.scope['url_route']['kwargs']['groupkaname']
        print("GROUP NAME   ....", self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,          #group name
            self.channel_name
            )
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        print('websocket Received from client.. ',event['text'])
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
            'type': 'chat.message',
            'message': event['text']
        })
    def chat_message(self,event):
        print('Event...',event)
        print('Actual data...',event['message'])
        self.send({
            'type':'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self,event):
        print('websocket disconneted.. ',event)
        print('Channel layer.. ', self.channel_layer)    #get default channel layer from a project
        print('Channel name.. ', self.channel_name)    #get default channel name from a projec
        
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
            )
        raise StopConsumer
    
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket Connected... ',event)
        print('Channel layer.. ', self.channel_layer)    #get default channel layer from a project
        print('Channel name.. ', self.channel_name)    #get default channel name from a project
        self.group_name=self.scope['url_route']['kwargs']['groupkaname']
        await self.channel_layer.group_add(
            self.group_name,          #group name
            self.channel_name
            )
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self,event):
        print('websocket Received from client.. ',event['text'])
        await self.channel_layer.group_send(self.group_name,{
            'type': 'chat.message',
            'message': event['text']
        })
    async def chat_message(self,event):
        print('Event...',event)
        print('Actual data...',event['message'])
        await self.send({
            'type':'websocket.send',
            'text': event['message']
        })

    async def websocket_disconnect(self,event):
        print('websocket disconneted.. ',event)
        print('Channel layer.. ', self.channel_layer)    #get default channel layer from a project
        print('Channel name.. ', self.channel_name)    #get default channel name from a projec
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
            )
        raise StopConsumer
    