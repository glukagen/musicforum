from django.conf.urls.defaults import *
from django.conf import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from forum.views import *

urlpatterns = patterns('',
    (r'^', include('forum.urls')),
    (r'^accounts/', include('registration.backends.default.urls') ),
    (r'^user/', include('_user.urls') ),
    (r'^band/', include('band.urls') ),
    (r'^review/', include('review.urls') ),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT} ), 
    (r'^admin/', include(admin.site.urls)),
)
