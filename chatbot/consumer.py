# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .utils import encontrar_respuesta  # Importa tu función de IA

class ChatbotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']

            # Envía un indicador de "escribiendo"
            await self.send(text_data=json.dumps({
                'type': 'status',
                'message': 'typing'
            }))

            # Envuelve la función síncrona en un wrapper asíncrono
            respuesta = await self.get_bot_response(message)
        
            # Obtiene respuesta usando tu lógica de chatbot
            #respuesta = encontrar_respuesta(message)
        
            await self.send(text_data=json.dumps({
                'type': 'message',
                'message': respuesta
            }))

        except Exception as e:
            """ await self.send(text_data=json.dumps({
                'type': 'error',
                'message': f'Error: {str(e)}' 
            }))"""
            pass

    @sync_to_async
    def get_bot_response(self, message):
        try:
            from django.db import reset_queries, close_old_connections
            close_old_connections()
            reset_queries()
            return encontrar_respuesta(message)
        finally:
            close_old_connections()