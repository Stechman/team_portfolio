from django.http import HttpResponse
from shortcuts import render_response
#shortcuts.py is baller file

def home(request):
    #return HttpResponse("POLL INDEX YOOO")
    return render_response('home.html')

def projects(request):
    return render_response('projects.html')
