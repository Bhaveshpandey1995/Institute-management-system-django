from django.contrib import admin
from django.urls import path, include
# import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account.views import dashboard
from home.views import *
from django.contrib.auth import views


admin.site.site_header = "MMMUT Admin"
admin.site.site_title = "MMMUT Admin Portal"
admin.site.index_title = "Welcome to MMMUT Portal"

urlpatterns = [
    # path('__debug__', include(debug_toolbar.urls)),
    path('logout/', views.LogoutView.as_view(template_name='registration/login.html')),
    path('admin/', admin.site.urls),
    # path('admin/', admin.site.urls, name='admin'),
    path('dashbord/', dashboard, name='index_view'),
    path('', IndexView, name='home'),
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('result/', include('result.urls')),
    path('misc/', include('admin_tools.urls')),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='account/password/password_reset.html'
        ),
        name="password_reset",
    ),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='account/password/password_reset_done.html'
        ),
        name="password_reset_done",
    ),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='account/password/password_reset_confirm.html'
        ),
        name='password_reset_confirm',
    ),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='account/password/password-reset-complete.html'
        ),
    name='password_reset_complete'
    ),
    path('course/', include('course.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
