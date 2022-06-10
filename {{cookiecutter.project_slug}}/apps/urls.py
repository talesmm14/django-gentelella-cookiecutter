from django.urls import path, include

urlpatterns = [
    path('auth/', include('apps.authentication.urls')),
    path('{{cookiecutter.app_title}}/', include('apps.{{cookiecutter.app_title}}.urls')),
    path('', include('apps.utils.urls')),
]
