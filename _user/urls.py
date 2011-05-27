from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('', 
    url(r'^(?P<username>[a-zA-Z0-9-_]*)/$', profile, name='UserInfo'),
)