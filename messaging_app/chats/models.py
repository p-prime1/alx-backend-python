from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

# Create your models here.


class user(AbstractUser):
    """Custo User model extending Django's AbstractUser"""

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.c = CharField(max_length=200)
    primary_key = TextField()

    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    profile_picture - models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )

    def __str__(self):
        return self.username


class Conversation:
    """Model tracks which users are involved in a conversation"""

    users = models.ManyToManyField(User, related_name="conversations")
    conversation_id = models.TextField(default=uuid.uuid4, editable=False, unique=True)
    particicpants = models.CharField(255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation ID: {self.conversation_id}"


class Message:
    """Model containing sender and conversation"""

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages"
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_messages",
    )
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="messages", null=True
    )
    message_id = models.TextField(default=uuid.uuid4, editable=False, unique=True)
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
