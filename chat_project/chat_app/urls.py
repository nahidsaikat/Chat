from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from chat_app import views

urlpatterns = [
    path('chat/', views.ChatList.as_view()),
    path('chat/<int:pk>/', views.ChatDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
