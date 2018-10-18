from django.contrib import admin
from chat.models import ChatRoom, AgentStatus

admin.site.register(ChatRoom)
admin.site.register(AgentStatus)
