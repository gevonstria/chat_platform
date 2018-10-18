from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from chat.models import ChatRoom, AgentStatus
import uuid

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

@method_decorator(csrf_exempt, name='dispatch')
class ChatNewView(View):

    def post(self, request):
        user_id = request.POST["user_id"]
        chat_type = request.POST["chat_type"]

        customer = User.objects.get(id=user_id)
        name = uuid.uuid4().hex[:16].upper()

        new_chat_room = ChatRoom()
        new_chat_room.name = name
        new_chat_room.customer = customer
        new_chat_room.type = chat_type
        new_chat_room.status = "on_queue"
        new_chat_room.save()

        return JsonResponse({'chat_room_name': name})

@method_decorator(csrf_exempt, name='dispatch')
class OnQueue(View):

    def get(self, request):
        data = AutoVivification()
        chat_room_list_on_queue = ChatRoom.objects.filter(status="on_queue")
        for chat_room in chat_room_list_on_queue:
            data[chat_room.id]["type"] = chat_room.type
            data[chat_room.id]["customer_id"] = chat_room.customer.id
            data[chat_room.id]["customer"] = chat_room.customer.username

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class IdleAgents(View):

    def get(self, request):
        data = AutoVivification()
        
        idle_agents = AgentStatus.objects.filter(status="idle")
        for idle_agent in idle_agents:
            data[idle_agent.agent.id]["username"] = idle_agent.agent.username
            data[idle_agent.agent.id]["group"] = idle_agent.agent.groups.values_list('name',flat=True)[0]
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class AssignAgents(View):

    def post(self, request):
        user = User.objects.get(id=request.POST["user_id"])
        chat_room = ChatRoom.objects.get(id=request.POST["chat_room_id"])
        chat_room.agent = user
        chat_room.save()

        agent_stat = AgentStatus.objects.get(agent=user)
        agent_stat.status = "queue"
        agent_stat.save()

        return JsonResponse({"message":"Chat Assigned Successfully!"})

@method_decorator(csrf_exempt, name='dispatch')
class AgentQueue(View):

    def get(self, request, user_id):
        data = AutoVivification()
        print(user_id)
        user = User.objects.get(id=user_id)
        print(user)
        chat_rooms_assigned = ChatRoom.objects.filter(agent=user)

        for chat_room in chat_rooms_assigned:
            data[chat_room.id]["name"] = chat_room.name

        return JsonResponse(data)
