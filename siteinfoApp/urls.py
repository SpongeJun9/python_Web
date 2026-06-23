from django.urls import path
from . import views

app_name = 'siteinfo'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('robomaster/', views.robomaster, name='robomaster'),
    path('technical/', views.technical, name='technical'),
    path('members/', views.members, name='members'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('resources/', views.resources, name='resources'),
    path('contact/', views.contact, name='contact'),
]
