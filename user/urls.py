from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('valida_cadastro/', views.validate_registration, name='validate_registration'),
]
