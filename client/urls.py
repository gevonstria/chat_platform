from django.urls import path, include

from client.views import ClientView

urlpatterns = [
    path('', ClientView.as_view()),
]