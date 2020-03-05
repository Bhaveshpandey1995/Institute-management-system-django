from django.urls import path, include
from . import views

from django.contrib.auth.urls import urlpatterns as default_url


app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

# urlpatterns += default_url
