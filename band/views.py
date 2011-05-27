from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from band.models import MusicGroup
from forum.models import View


@login_required
def profile(request, id, template='band/profile.html'):
    try:
        group = MusicGroup.objects.get(id=id)
    except:
        return Http404
    view, response = View.objects.get_or_create(user=request.user, group=group)
    view.refresh()

    return render_to_response(template, {'group': group}, 
        context_instance=RequestContext(request))
    

@login_required
def review(request, id, template='band/review.html'):
    try:
        group = MusicGroup.objects.get(id=id)
    except:
        return Http404
    
    return render_to_response(template, {'group': group}, 
        context_instance=RequestContext(request))