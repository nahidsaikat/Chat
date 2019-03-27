from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Chat(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='from_chats')
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='to_chats')
    message = models.TextField(verbose_name='Message', default='')
