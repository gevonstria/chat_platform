# chat/routing.py
from django.conf.urls import url
from django.urls import path
from chat import customers

websocket_urlpatterns = [
    path('ws/chat/<room_name>/', customers.ChatCustomer),
]