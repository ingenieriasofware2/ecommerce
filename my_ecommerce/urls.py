"""
Su función es definir las rutas de URL de la aplicación y especificar cómo se 
relacionan con las vistas y funcionalidades correspondientes.

El archivo urls.py en Django se considera una INTERFACE. Este archivo define 
las rutas de URL y cómo se relacionan con las vistas correspondientes. 
Proporciona una interfaz para mapear las URL de la aplicación a las 
funcionalidades y vistas específicas que deben ejecutarse cuando se accede a esas URL.

URL configuration for my_ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('access.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
    
]