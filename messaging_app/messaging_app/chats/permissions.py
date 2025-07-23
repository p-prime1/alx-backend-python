from rest_framework.permissions import BasePermission
from .models import Conversation


class IsParticipantInConversation(BasePermission):
    def has_object_permission(self, request, view, obj):
        conversation = obj.conversation if hasattr(obj, 'conversation') else obj
        return conversation.participants.filter(id=request.user.id).exists()



class IsMessageSender(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.sender_id == request.user.id