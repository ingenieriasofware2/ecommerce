"""
Su función es proporcionar una interfaz de comunicación entre el servidor web y la aplicación Django.

el archivo wsgi.py actúa como un ADAPTADOR entre el servidor web y la aplicación Django. 
Proporciona una interfaz WSGI (Web Server Gateway Interface) que el servidor web puede utilizar 
para comunicarse con la aplicación Django. El servidor web se conecta al archivo wsgi.py y 
utiliza la interfaz WSGI para enviar solicitudes HTTP a la aplicación y recibir las respuestas correspondientes.

WSGI config for my_ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_ecommerce.settings')

application = get_wsgi_application()
