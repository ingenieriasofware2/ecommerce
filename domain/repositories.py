from abc import ABC, abstractmethod

"""define las interfaces UserRepository, CategoryRepository, 
ProductRepository y OrderRepository utilizando la clase 
abstracta ABC del módulo abc. Cada interfaz define los 
métodos necesarios para realizar operaciones relacionadas 
con los respectivos modelos.
"""

class UserRepository(ABC):
    @abstractmethod
    def create_user(self, username, email, password):
        pass

    @abstractmethod
    def get_user_by_username(self, username):
        pass

    @abstractmethod
    def get_user_by_email(self, email):
        pass

    @abstractmethod
    def update_user_password(self, user):
        pass

    @abstractmethod
    def delete_user(self, user):
        pass

class CategoryRepository(ABC):
    @abstractmethod
    def create_category(self, name, description):
        pass

    @abstractmethod
    def get_category_by_name(self, name):
        pass


class ProductRepository(ABC):
    @abstractmethod
    def create_product(self, name, description, price, category):
        pass

    @abstractmethod
    def get_product_id_by_name(self, name):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def update_product_price(self, product):
        pass

    @abstractmethod
    def delete_product(self, product):
        pass


class OrderRepository(ABC):
    @abstractmethod
    def create_order(self, user):
        pass

    @abstractmethod
    def add_product_to_order(self, order, product, quantity):
        pass
