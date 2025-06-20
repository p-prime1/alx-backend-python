from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]  # ❌ Fixed: 'permission' → 'permissions'

    def perform_create(self, serializer):
        conversation = serializer.save()
        conversation.participants.add(self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        conversation_id = self.request.query_params.get('conversation')  # ❌ Fixed: 'conversations' → 'conversation'
        if conversation_id:
            return Message.objects.filter(conversation__conversation_id=conversation_id)
        return Message.objects.none()

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
