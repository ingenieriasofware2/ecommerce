"""los adaptadores de repositorio deben encapsular los 
detalles específicos de la base de datos y proporcionar 
entidades o modelos de dominio más abstractos a las 
capas superiores.
"""
from domain.models import User

from domain.repositories import UserRepository
from django.contrib.auth.models import User as DjangoUser

class DatabaseUserRepository(UserRepository):
    def create_user(self, username, email, password):
        django_user = DjangoUser.objects.create_user(username=username, email=email, password=password)
        self._map_django_user_to_domain_model(django_user)
        # Realizar cualquier otro procesamiento o validación adicional si es necesario
        # ...

    def _map_django_user_to_domain_model(self, django_user):
        user = User(
            id=django_user.id,
            username=django_user.username,
            email=django_user.email,
            # Mapear otros atributos según sea necesario
        )
        return user
    
    def get_user_by_username(self, username):
        try:
            django_user = DjangoUser.objects.get(username=username)
            user = self._map_django_user_to_domain_model(django_user)
            return user
        except DjangoUser.DoesNotExist:
            return None

    def get_user_by_email(self, email):
        try:
            django_user = DjangoUser.objects.get(email=email)
            user = self._map_django_user_to_domain_model(django_user)
            return user
        except DjangoUser.DoesNotExist:
            return None

    def update_user_password(self, user):
        django_user = DjangoUser.objects.get(id=user.id)
        django_user.set_password(user.password)
        django_user.save()
        # Realizar cualquier otro procesamiento o validación adicional si es necesario
        # ...
        return user

    def delete_user(self, user):
        django_user = DjangoUser.objects.get(id=user.id)
        django_user.delete()
        # Realizar cualquier otro procesamiento o validación adicional si es necesario
        # ...
