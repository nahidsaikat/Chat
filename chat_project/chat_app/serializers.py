from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'to_user', 'message')

    def validate(self, data):
        # verify te initial data types by calling super
        # super().validate(data)
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        data['from_user'] = user
        return data
