from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

class ClientView(View):

    def get(self, request):
        user_id = request.user.id
        return render(request, 'client.html', {"user_id": user_id })