from django.shortcuts import render
from django.http import HttpResponse , Http404
# Create your views here.
def home(request):
    return render(request , "blog/home.html")

def course(request , slug):
    if slug == "Django":
        return render(request , "blog/django.html")
    elif slug == "Json":
        return render(request , "blog/json.html")
    elif slug == "Html":
        return render(request , "blog/html.html")
    else :
        raise Http404("You are lost")
def any(request , any):
    raise Http404("You are lost")