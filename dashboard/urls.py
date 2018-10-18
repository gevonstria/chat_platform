from django.urls import path, include

from dashboard.views import DashboardView, AgentDashboardView

urlpatterns = [
	path('', DashboardView.as_view()),
    path('agent', AgentDashboardView.as_view()),
    path('agent/<room_name>', AgentDashboardView.as_view()),
]