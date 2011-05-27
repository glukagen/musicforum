from django.db import models
from django.contrib.auth.models import User


class MusicGroup(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=300)
    added = models.DateTimeField(auto_now_add=True)