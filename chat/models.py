from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="customer")
    agent = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="agent")
    status = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.type) +" - " +str(self.customer.username)

    class Meta:
        verbose_name = 'Chat Room'
        verbose_name_plural = 'Chat Rooms'


class AgentStatus(models.Model):
    agent = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.agent.username) +" - " +str(self.status)

    class Meta:
        verbose_name = 'Agent Status'
        verbose_name_plural = 'Agent Status'