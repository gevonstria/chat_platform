from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from chat.models import ChatRoom, AgentStatus
from django.http import JsonResponse
from django.http import HttpResponseRedirect

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

class DashboardView(View):

    def get(self, request):
        username = request.user.username
        data = AutoVivification()

        return render(request, 'dashboard.html', {"username": username })


class AgentDashboardView(View):

    def get(self, request, room_name):
        username = request.user.username
        user_id = request.user.id

        if not room_name == "default":
            agent_stat = AgentStatus.objects.get(agent=request.user)
            agent_stat.status = "chat"
            agent_stat.save()

        return render(request, 'agent_dashboard.html', {"username": username, "user_id": user_id, "room_name": room_name})