from django.urls import path
from . import views
app_name = 'empresas'  # Nombre de la aplicación

urlpatterns = [
    path('crear/', views.crear_empresa, name='crear_empresa'),
]