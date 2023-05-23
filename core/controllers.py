from infraestructura.adapters import DatabaseUserRepository
from core.services import UserService

"""
# Instanciar el repositorio
user_repository = DatabaseUserRepository()

# Instanciar el servicio y pasarle el repositorio
user_service = UserService(user_repository)

# Llamar a los métodos del servicio
username = "john_doe"
email = "john.doe@example.com"
password = "password123"

user_service.create_user(username, email, password)
"""
from domain.models import User
from domain.repositories import UserRepository
from core.services import UserService

class UserController:
    def __init__(self, user_repository: UserRepository):
        self.user_service = UserService(user_repository)#servicio

    def create_user(self, username: str, email: str, password: str) -> User:
        return self.user_service.create_user(username, email, password)

    def get_user(self, user_id: int) -> User:
        return self.user_service.get_user(user_id)

    def update_user(self, user_id: int, username: str, email: str) -> User:
        return self.user_service.update_user(user_id, username, email)

    def delete_user(self, user_id: int):
        self.user_service.delete_user(user_id)
