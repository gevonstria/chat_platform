from django.urls import path, include

from chat.views import ChatNewView, OnQueue, IdleAgents, AssignAgents, AgentQueue

urlpatterns = [
    path('new', ChatNewView.as_view()),
    path('on_q', OnQueue.as_view()),
    path('assign', AssignAgents.as_view()),
    path('agents/idle', IdleAgents.as_view()),
    path('agents/queue/<user_id>', AgentQueue.as_view()),
]