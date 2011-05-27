from django.db import models
from django.contrib.auth.models import User
from band.models import *
from _user.models import *
import datetime


class Feedback(models.Model):
    group = models.ForeignKey(MusicGroup)
    user = models.ForeignKey(User)
    
    timeFollowed = models.IntegerField(null=True, blank=True)
    timeListen = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    soundQuality = models.IntegerField(null=True, blank=True)
    coolness = models.IntegerField(null=True, blank=True)
    freshness = models.IntegerField(null=True, blank=True)
    

class View(models.Model):
    group = models.ForeignKey(MusicGroup)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    
    def refresh(self):
        self.date = datetime.datetime.now()
        self.save()
    