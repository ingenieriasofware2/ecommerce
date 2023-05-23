"""
Actua como un adaptador que conecta la aplicación Django con el servidor 
ASGI. Proporciona una interfaz para exponer la aplicación como un servidor 
compatible con ASGI, lo que permite la comunicación asincrónica y el 
manejo eficiente de solicitudes y respuestas en entornos de producción.

ASGI config for my_ecommerce project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_ecommerce.settings')

application = get_asgi_application()
