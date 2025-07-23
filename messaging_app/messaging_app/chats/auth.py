from .models import Conversation, Message


def user_permissions(user, conversation):
    return conversation.participants.filter(id=user.id).exists()