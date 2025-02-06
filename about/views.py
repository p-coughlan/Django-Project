from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_me(request):
    """
    This is the view that will be called when the user visits the /about URL of the site.
    """
    return HttpResponse("This would be the about page")