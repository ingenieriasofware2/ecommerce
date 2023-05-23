from django.test import TestCase
from decimal import Decimal
from django.contrib.auth.hashers import make_password, check_password


from domain.models import Category
from domain.models import User
from domain.models import Product,Order, OrderItem

from services import create_order, get_order_by_id, get_orders_by_user, update_order_total_price, delete_order
from services import create_category, get_category_by_name, get_category_description_by_name
from services import create_product, get_product_id_by_name,get_product_by_id, update_product_price, delete_product
from .services import create_user, get_user_by_username, get_user_by_email, update_user_password, delete_user

from infraestructura.adapters import DatabaseUserRepository
from core.services import UserService

import unittest
from unittest.mock import MagicMock
from controllers import UserController


class UserControllerTestCase(unittest.TestCase):
    
    def test_create_user(self):
        # Mockear el repositorio
        user_repository = MagicMock()
        print('hola')
        # Instanciar el controlador y pasarle el repositorio
        user_controller = UserController(user_repository)

        # Datos de ejemplo
        username = "john_doe"
        email = "john.doe@example.com"
        password = "password123"

        # Llamar al método del controlador
        user_controller.create_user(username, email, password)

      

if __name__ == "__main__":
    unittest.main()


class OrderServiceTest(TestCase):
    print('TEST DE SERVICIOS - PRODUCTOS')
    def setUp(self):
        # Crear un usuario para utilizar en las pruebas
        self.user = User.objects.create(username='testuser', email='test@example.com', password='password')

        # Crear algunos productos para utilizar en las pruebas
        self.product1 = Product.objects.create(name='Product 1', description='Description 1', price=10.99)
        self.product2 = Product.objects.create(name='Product 2', description='Description 2', price=19.99)

    def test_create_order(self):
        # Crear una orden con productos y verificar que se haya creado correctamente
        products = [(self.product1, 2), (self.product2, 3)]
        total_price = 99.99
        order = create_order(self.user, products, total_price)
        self.assertIsInstance(order, Order)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.total_price, total_price)
        self.assertEqual(order.orderitem_set.count(), len(products))

    def test_get_order_by_id(self):
        # Crear una orden y luego obtenerla por su ID y verificar que sea la misma
        order = create_order(self.user, [], 0.0)
        retrieved_order = get_order_by_id(order.id)
        self.assertEqual(order, retrieved_order)

    def test_get_orders_by_user(self):
        # Crear varias órdenes para un usuario y luego obtener todas las órdenes del usuario
        order1 = create_order(self.user, [], 0.0)
        order2 = create_order(self.user, [], 0.0)
        orders = get_orders_by_user(self.user)
        self.assertIn(order1, orders)
        self.assertIn(order2, orders)
        self.assertEqual(len(orders), 2)

    def test_update_order_total_price(self):
        # Crear una orden y luego actualizar su precio total y verificar que se haya actualizado correctamente
        order = create_order(self.user, [], 0.0)
        new_total_price = 199.99
        success = update_order_total_price(order.id, new_total_price)
        self.assertTrue(success)
        updated_order = get_order_by_id(order.id)
        self.assertEqual(updated_order.total_price, new_total_price)

    def test_delete_order(self):
        # Crear una orden y luego eliminarla y verificar que se haya eliminado correctamente
        order = create_order(self.user, [], 0.0)
        success = delete_order(order.id)
        self.assertTrue(success)
        deleted_order = get_order_by_id(order.id)
        self.assertIsNone(deleted_order)

class ProductServicesTest(TestCase):
    print('TEST DE SERVICIOS - PRODUCTOS')
    def setUp(self):
        # Crea una categoría para utilizarla en las pruebas
        self.category = Category.objects.create(name='Electronics', description='Electronics category')

    def test_create_product(self):
        product = create_product(name='Smartphone', description='A high-end smartphone', price=999.99, category=self.category)
        self.assertIsNotNone(product.id)
    
    def test_get_product_id_by_name(self):
        product = Product.objects.create(name='Smartphone', description='A high-end smartphone', price=999.99, category=self.category)
        retrieved_product_id = get_product_id_by_name('Smartphone')

        self.assertEqual(retrieved_product_id, product.id)
        print('id product: ', product.id)
  

    def test_get_product_id_by_name_nonexistent(self):
        retrieved_product_id = get_product_id_by_name('Nonexistent Product')
        self.assertIsNone(retrieved_product_id)

    def test_get_product_by_id(self):
        product = create_product(name='Smartphone', description='A high-end smartphone', price=999.99, category=self.category)
        retrieved_product = get_product_by_id(product.id)
        self.assertEqual(retrieved_product, product)

    def test_update_product_price(self):
        product = create_product(name='Smartphone', description='A high-end smartphone', price=999.99, category=self.category)
        updated_price = Decimal('899.99')
        success = update_product_price(product.id, updated_price)
        self.assertTrue(success)
        retrieved_product = get_product_by_id(product.id)
        self.assertEqual(retrieved_product.price, updated_price)

    def test_delete_product(self):
        product = create_product(name='Smartphone', description='A high-end smartphone', price=999.99, category=self.category)
        success = delete_product(product.id)
        self.assertTrue(success)
        retrieved_product = get_product_by_id(product.id)
        self.assertIsNone(retrieved_product)

class CategoryServiceTest(TestCase):
    print('TEST DE SERVICIOS - CATEGORY')
    def setUp(self):
        self.category_name = 'Electronics'
        self.category_description = 'Electronics category'

    def test_create_category(self):
        category = create_category(self.category_name, self.category_description)

        self.assertIsInstance(category, Category)
        self.assertEqual(category.name, self.category_name)
        self.assertEqual(category.description, self.category_description)

    def test_get_category_by_name(self):
        create_category(self.category_name, self.category_description)

        category = get_category_by_name(self.category_name)

        self.assertIsInstance(category, Category)
        self.assertEqual(category.name, self.category_name)
        self.assertEqual(category.description, self.category_description)

    def test_get_category_description_by_name(self):
        create_category(self.category_name, self.category_description)

        description = get_category_description_by_name(self.category_name)

        self.assertEqual(description, self.category_description)


class UserServiceTest(TestCase):
    print('TEST DE SERVICIOS - USER')
    def test_create_user(self):
        username = 'john'
        email = 'john@example.com'
        password = 'password'

        # Crea un usuario
        user = create_user(username, email, password)

        # Verifica que el usuario se haya guardado correctamente
        saved_user = get_user_by_username(username)
        self.assertEqual(user, saved_user)

    def test_get_user_by_username(self):
        username = 'john'
        email = 'john@example.com'
        password = 'password'

        # Crea un usuario
        user = create_user(username, email, password)

        # Obtiene el usuario por nombre de usuario
        found_user = get_user_by_username(username)

        # Verifica que el usuario retornado sea el correcto
        self.assertEqual(user, found_user)

    def test_get_user_by_email(self):
        username = 'john'
        email = 'john@example.com'
        password = 'password'

        # Crea un usuario
        user = create_user(username, email, password)

        # Obtiene el usuario por correo electrónico
        found_user = get_user_by_email(email)

        # Verifica que el usuario retornado sea el correcto
        self.assertEqual(user, found_user)

    def test_update_user_password(self):
        username = 'john'
        email = 'john@example.com'
        password = 'password'
        new_password = 'newpassword'

        user = create_user(username, email, password)

        # Actualiza la contraseña del usuario
        updated = update_user_password(username, new_password)

        # Verifica que la contraseña se haya actualizado correctamente
        self.assertTrue(updated)

        # Obtiene el usuario actualizado
        updated_user = get_user_by_username(username)

        # Verifica que la contraseña del usuario actualizado sea la correcta
        self.assertEqual(new_password, updated_user.get_password())

    def test_delete_user(self):
        username = 'john'
        email = 'john@example.com'
        password = 'password'

        # Crea un usuario
        create_user(username, email, password)

        # Elimina el usuario
        deleted = delete_user(username)

        # Verifica que el usuario se haya eliminado correctamente
        self.assertTrue(deleted)

        # Intenta obtener el usuario eliminado
        deleted_user = get_user_by_username(username)

        # Verifica que el usuario eliminado no exista
        self.assertIsNone(deleted_user)

