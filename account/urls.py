from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

from django.contrib.auth.urls import urlpatterns as default_url


app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('student/', auth_view.LoginView.as_view(template_name='registration/studentlogin.html'), name='student_login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('studentdashboard/', views.dashboard, name='studentdashboard'),
    
]

# urlpatterns += default_url
