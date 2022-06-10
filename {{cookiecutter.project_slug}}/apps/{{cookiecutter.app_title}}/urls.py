from django.urls import path
from apps.{{cookiecutter.app_title}} import views

urlpatterns = [
     path('{{cookiecutter.app_class_name}}/', views.{{cookiecutter.app_class_name}}_view),
]