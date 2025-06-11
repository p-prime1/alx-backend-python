from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class user(AbstractUser):
    """Model for the user"""

    Name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    profile_picture - models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user_name


class conversation:
    """Model tracks which users are involved in a conversation"""

    users = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation ID: {self.id}"


class message:
    """Model containing sender and conversation"""

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages"
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_messages",
    )
    body = models.TextField()
