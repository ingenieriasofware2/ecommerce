from django.test import TestCase
from decimal import Decimal
from django.contrib.auth.hashers import make_password, check_password


from domain.models import Category
from domain.models import User
from domain.models import Product,Order, OrderItem

class UserTest(TestCase):
    def test_create_user(self):
        print("TEST DE USUARIO CREACION Y GUARDADO EN BD ENTIDADES")
        # Crea un usuario
        user1 = User(username='john', email='john@example.com', password='password')
        user1.save()

        # Verifica que el usuario se haya guardado correctamente
        saved_user = User.objects.get(username='john')
        self.assertEqual(user1, saved_user)
        print("usuario creado ", user1.get_username(), "usuario guardado ", saved_user.get_username())


class ProductTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics', description='Electronics category')
        self.product = Product.objects.create(
            name='Smartphone',
            description='A high-end smartphone',
            price=999,
            category=self.category
        )

    def test_get_name(self):
        self.assertEqual(self.product.get_name(), 'Smartphone')

    def test_get_description(self):
        self.assertEqual(self.product.get_description(), 'A high-end smartphone')

    def test_get_price(self):
        expected_price = 999
        self.assertEqual(self.product.get_price(), expected_price)

    def test_get_category(self):
        self.assertEqual(self.product.get_category(), self.category)


class OrderTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='john', email='john@example.com', password='password')
        category1 = Category.objects.create(name='Electronics', description='Electronics category')
        product1 = Product.objects.create(
            name='Smartphone',
            description='A high-end smartphone',
            price=999.99,
            category=category1
        )
        product2 = Product.objects.create(
            name='TV',
            description='A high-end TV',
            price=9999.99,
            category=category1
        )

        self.order = Order.objects.create(user=user, total_price=29.98)
        order_item1 = OrderItem.objects.create(order=self.order, product=product1, quantity=1)
        order_item2 = OrderItem.objects.create(order=self.order, product=product2, quantity=2)

    def test_get_user(self):
        user = self.order.get_user()
        self.assertEqual(user.get_username(), 'john')

    def test_get_products(self):
        products = self.order.get_products()
        self.assertEqual(products.count(), 2)

    def test_calculate_total_price(self):
        self.order.calculate_total_price()
        expected_total_price = Decimal('20999.97')
        self.assertEqual(self.order.get_total_price(), expected_total_price)

    def test_get_created_at(self):
        created_at = self.order.get_created_at()
        self.assertIsNotNone(created_at)