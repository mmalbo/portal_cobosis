from django.urls import path
from .views import chatbot_api, ChatbotAuthAPI, ChatbotPrivateAPI

urlpatterns = [
    path('api/chatbot/', chatbot_api, name='chatbot_api'),
    path('api/chatbot/auth/', ChatbotAuthAPI.as_view(), name='chatbot_auth'),
    path('api/chatbot/private/', ChatbotPrivateAPI.as_view(), name='chatbot_private'),
]