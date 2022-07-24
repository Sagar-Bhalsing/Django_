from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "Developer Sagar"
admin.site.site_title = "Welcome to Dasboard"
admin.site.index_title = "Welcome to Portal"
urlpatterns = [ 
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
]