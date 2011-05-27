from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from forum.models import View
from _user.models import UserProfile


@login_required
def profile(request, username, template='_user/profile.html'):
    print request.user
    try:
        profile = UserProfile.objects.get(user__username=username)
    except:
        return Http404
    views = View.objects.filter(user=profile.user).order_by('-date')[:20]
    return render_to_response(template, {'user': profile, 'views': views}, 
        context_instance=RequestContext(request))    