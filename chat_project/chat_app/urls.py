from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from chat_app import views

urlpatterns = [
    path('chat/', views.ChatList.as_view(), name="list_create"),
    path('chat/<int:pk>/', views.ChatDetail.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
