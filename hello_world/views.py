from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """
    This is the view that will be called when the user visits the root URL of the site.
    """
    return HttpResponse("Hello, world!")