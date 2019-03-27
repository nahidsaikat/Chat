from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'to_user', 'message')

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        validated_data['from_user'] = user
        return super().create(validated_data)
