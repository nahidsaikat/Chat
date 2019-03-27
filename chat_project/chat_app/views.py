from chat_app.models import Chat
from chat_app.serializers import ChatSerializer
from chat_app.permissions import IsOwnerOrReadOnly
from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response


class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def list(self, request, *args, **kwargs):
        # Could overwrite the get_queryset method instead
        queryset = self.filter_queryset(self.get_queryset())

        if request.user.id:
            queryset = queryset.filter(Q(from_user=request.user) | Q(to_user=request.user))
        else:
            queryset = Chat.objects.none()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    # Could override the IsAuthenticatedOrReadOnly permission class instead for IsOwnerOrReadOnly
    # That way you'd require one permission less
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)




