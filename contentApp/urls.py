from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('robots/', views.robots, name='robots'),
    path('robots/<int:pk>/', views.robot_detail, name='robot_detail'),
    path('robots/demo/<slug:slug>/', views.robot_default_detail, name='robot_default_detail'),
    path('achievements/', views.achievements, name='achievements'),
    path('news/', views.news, name='news'),
    path('news/search/', views.news_search, name='news_search'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news/demo/<slug:slug>/', views.news_default_detail, name='news_default_detail'),
]
