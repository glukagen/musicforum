from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, db_index=True)
    bithdate = models.DateField()
    location = models.CharField(max_length=300, null=True, blank=True)
    rating =  models.DecimalField(max_digits=5, decimal_places=2)
    website = models.URLField(max_length=300, null=True, blank=True)
    facebook = models.CharField(max_length=300, null=True, blank=True)
    twitter = models.CharField(max_length=300, null=True, blank=True)
    linkedin = models.CharField(max_length=300, null=True, blank=True)