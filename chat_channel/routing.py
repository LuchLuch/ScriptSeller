from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat_channel/<str:room_name>/', consumers.ChatConsumer),
]