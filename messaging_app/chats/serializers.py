form rest_framework import serializers
from .models import User, Conversation, Message
from rest_framework.serializers import CharField, SerializerMethodField, ValidationError


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = '__all__'

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'

    def validate_message_body(self, value):
        if 'badword' in value.lower():
            raise serializers.ValidationError("Inappropriate content detected.")
        return value


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Conversation
        fields = '__all__'
