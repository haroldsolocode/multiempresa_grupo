"""
Configuraciones de Django para el proyecto Multiempresa.

Este módulo configura la aplicación Django, incluyendo la base de datos, 
aplicaciones instaladas, middleware, plantillas y autenticación.
"""

"""
Django settings for Multiempresa project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent # Cambia la ruta del directorio base si es necesario (por defecto es el directorio del proyecto)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*8u8_10pcu)@phusz+*kxkdnvdb96g!ny#t1$63x876))dqf&+' # Cambia esta clave en producción

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Cambia a False en producción

ALLOWED_HOSTS = [] # Agrega aquí los hosts permitidos


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'roles',
    'seguridad',
    # Agregamos la app que creamos
    
]
AUTH_USER_MODEL = 'usuarios.Usuario'  # Cambia el modelo de usuario por defecto de Django

AUTHENTICATION_BACKENDS = [ # Configura los backends de autenticación
    'usuarios.backends.EmailBackend',  # Agrega tu backend personalizado aquí
    'django.contrib.auth.backends.ModelBackend',  # Mantén el backend por defecto de Django
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # Configuración para enviar correos electrónicos en consola (para pruebas)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] # Configura los middleware de Django (intermediarios de las peticiones)   

ROOT_URLCONF = 'Multiempresa.urls' # Configura el archivo de rutas principal

TEMPLATES = [ # Configura las plantillas de Django
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True, # Habilita la carga de plantillas desde las aplicaciones
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Multiempresa.wsgi.application' # Configura la aplicación WSGI para despliegue en servidores web


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = { # Configura la base de datos de Django
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Cambiamos SQLite por MySQL
        'NAME': 'multiempresa',  # Nombre de la base de datos en MySQL
        'USER': 'root',       # Usuario de MySQL
        'PASSWORD': '', # Contraseña de MySQL
        'HOST': 'localhost',        # Dirección del servidor MySQL (usa IP si es remoto)
        'PORT': '3306',             # Puerto de MySQL (3306 por defecto)
        'OPTIONS':{         # Opciones adicionales de MySQL
        'init_command': "SET sql_mode= 'STRICT_TRANS_TABLES'", # Configura el modo estricto de MySQL para evitar errores 
        },  
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [ # Configura las validaciones de contraseñas
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Configura el tipo de campo de clave primaria por defecto de Django  

LOGIN_URL = '/usuarios/login/' # Configura la URL de inicio de sesión



