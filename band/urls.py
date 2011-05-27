from django.conf.urls.defaults import *

from views import * 

urlpatterns = patterns('',
      url(r'^(?P<id>\d+)/$', profile, name='groupProfile'),
      url(r'^(?P<id>\d+)/review/$', review, name='groupReview'),
)
