from django.urls import path
from . import views

app_name = 'recruitment'

urlpatterns = [
    path('recruitment/', views.recruitment, name='recruitment'),
    path('recruitment/success/', views.success, name='success'),
]
