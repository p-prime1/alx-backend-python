from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .auth import user_permissions  # Make sure this is defined correctly
from .permissions import IsParticipantInConversation, IsMessageSender

# Create your views here.


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantInConversation]

    def get_queryset(self):
        # Only return conversations the user is a part of
        return Conversation.objects.filter(participants=self.request.user)

    def perform_create(self, serializer):
        # Save conversation and add current user as a participant
        conversation = serializer.save()
        conversation.participants.add(self.request.user)



class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantInConversation]

    def get_queryset(self):
        return Message.objects.filter(conversation_participants=self.request.user)

    def perform_create(self, serializer):
        conversation = serializer.validated_data['conversation']
        if self.request.user not in conversation.participants.all():
            raise PermissionDenied("You are not a participant")

            if not user_permission(self.request.user, conversation):
                raise PermissionDenied("You do nat have permission to send a message")

        serializer.save(sender=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsMessageSender()]

        return super().get_permissions()
