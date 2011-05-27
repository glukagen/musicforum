from django.contrib import admin
from band.models import *


class MusicGroupAdmin(admin.ModelAdmin):
    model = MusicGroup
    list_display = ('owner', 'name',)
        

admin.site.register(MusicGroup, MusicGroupAdmin)