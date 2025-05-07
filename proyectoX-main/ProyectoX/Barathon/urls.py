from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Ruta para la página principal
    path('registro/', views.registro, name='registro'),  # Ruta para registro
    path('login/', views.login_view, name='login'),  # Ruta para login
]
