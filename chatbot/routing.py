from django.urls import re_path
from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/chatbot/$', consumer.ChatbotConsumer.as_asgi()),
]