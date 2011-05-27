from django.http import HttpResponse, Http404

def Index(request):
    return HttpResponse('Index')

