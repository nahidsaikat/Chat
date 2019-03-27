from chat_app.models import Chat
from chat_app.serializers import ChatSerializer
from chat_app.permissions import CustomIsAuthenticatedOrReadOnly
from django.db.models import Q
from rest_framework import generics


class ChatList(generics.ListCreateAPIView):
    """
    Can user IsAuthenticated permission that way
    you can be sure that a request user will always
    be available in the class
    """
    serializer_class = ChatSerializer

    def get_queryset(self):
        if self.request.user.id:
            queryset = Chat.objects.filter(Q(from_user=self.request.user) | Q(to_user=self.request.user))
        else:
            queryset = Chat.objects.none()
        return queryset


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    # Could override the IsAuthenticatedOrReadOnly permission class instead for IsOwnerOrReadOnly
    # That way you'd require one permission less
    permission_classes = (CustomIsAuthenticatedOrReadOnly,)
