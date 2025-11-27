# apikeys/models.py

import uuid
from django.db import models
from django.contrib.auth.models import User

def generate_api_key():
    return str(uuid.uuid4()).replace('-', '')[:50]

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_keys')
    name = models.CharField(max_length=50, help_text="e.g. Postman, Mobile App, Frontend")
    key = models.CharField(max_length=100, unique=True, default=generate_api_key)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.key[:15]}..."

    class Meta:
        verbose_name = "API Key"
        verbose_name_plural = "API Keys"