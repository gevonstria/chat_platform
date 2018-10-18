from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


class LogInView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
        else:
            error = "Invalid username/password"
            return render(request, "login.html", {"error": error})
