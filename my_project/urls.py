"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hello_world import views as index_views # Import the views module from the hello_world app using the alias index_views.
from about import views as about_views # Import the views module from the about app using the alias about_views.

urlpatterns = [
    path('hello/', index_views.index, name='index'), # Add a URL pattern to the urlpatterns list that maps the root URL of the site to the index view.
    path('about/', about_views.about_me, name='about'), # Add a URL pattern to the urlpatterns list that maps the /about URL of the site to the about_me view.
    path('admin/', admin.site.urls), # Why is this at the end? Because Django will check each URL pattern in the order they are defined in the urlpatterns list. If the admin URL pattern was defined before the hello/ and about/ URL patterns, Django would never reach the hello/ and about/ URL patterns because the admin URL pattern would match first.
]
