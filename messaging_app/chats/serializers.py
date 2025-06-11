from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'username', 'email', 'profile_picture']


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = conversation
        fields = ['conversation_id', 'particicpants', 'created_at', 'updated_at']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message_body
        fields = ['sender', 'recepient', 'conversation', 'message_body', 'message_id', 'sent_at']