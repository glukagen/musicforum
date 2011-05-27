from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from views import * 

"""
This function passes the context to the template
This allows access to basic system settings
Such as the media path.
"""
def direct_to_template_context(request,*args,**kwargs):
    kwargs['context_instance'] = RequestContext(request)
    return direct_to_template(request,*args,**kwargs)

urlpatterns = patterns('',

    url(r'^$', Index, name='Index'),
    url(r'^tos/$', direct_to_template, {'template': 'tos.html'}, name='TOS'),
    url(r'^welcome/$', direct_to_template, {'template': 'help.html', 'extra_context' : {'welcome': True}}, name='Welcome'),
)
