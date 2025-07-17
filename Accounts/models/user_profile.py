from django.db import models

class LoginLog(models.Model):
    user = models.ForeignKey('UniUser', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)