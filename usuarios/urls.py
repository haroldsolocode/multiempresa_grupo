"""
Configuración de URL para la aplicación 'usuarios'.

Este módulo define los patrones de URL específicos de la aplicación 'usuarios'.
"""
from django.urls import path # Importa la función 'path' para definir las URL
from . import views     # Importa las vistas definidas en el módulo 'views.py'

app_name = 'usuarios'  # Nombre de la aplicación

urlpatterns = [
    path('recuperar_contrasena/', views.recuperar_contrasena_view, name='recuperar_contrasena'),    # URL para la vista de recuperación de contraseña
    path('restablecer_contrasena/<int:usuario_id>/<str:token>/', views.restablecer_contrasena_view, name='restablecer_contrasena'), # URL con parámetros de ruta dinámicos (usuario_id y token)
    path('cambio_contrasena/', views.cambio_contrasena_view, name='cambio_contrasena'), # URL para la vista de cambio de contraseña
    path('registro/', views.register_view, name='registro'),    # URL para la vista de registro de usuario
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'), # URL para la vista de registro exitoso
    path('logout/', views.logout_view, name='logout'),  # URL para la vista de cierre de sesión
    path('admin_usuarios/', views.admin_usuarios_view, name='admin_usuarios'),  # URL para la vista de administración de usuarios
]


