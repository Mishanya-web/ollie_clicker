import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Gamer
from asgiref.sync import sync_to_async

class ButtonConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            self.user = self.scope["user"]
            self.session_clicks = 0
            self.player, _ = await sync_to_async(Gamer.objects.get_or_create)(user=self.user)

            await self.accept()

            self.periodic_task = asyncio.create_task(self.save_score_periodically())

    async def disconnect(self, close_code):

        self.periodic_task.cancel()

        self.player.score += self.session_clicks
        await sync_to_async(self.player.save)()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')

        if message == 'pressed':
            self.session_clicks += 1

        await self.send(text_data=json.dumps({
            'message': f'{self.session_clicks + self.player.score}'
        }))

    async def save_score_periodically(self):
        while True:
            await asyncio.sleep(0.1)
            self.player.score += self.session_clicks
            await sync_to_async(self.player.save)()
            self.session_clicks = 0
