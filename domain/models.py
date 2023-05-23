from django.db import models
"""los modelos se definen mediante la clase Model del módulo 
models de django.db. Esta clase proporciona métodos y atributos 
que permiten la interacción con la base de datos, como la 
definición de campos (como CharField, EmailField, DecimalField, 
DateTimeField, etc.) y las relaciones entre modelos 
(como ForeignKey, ManyToManyField, etc.).

"""

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_category(self):
        return self.category


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"

    def get_user(self):
        return self.user

    def get_products(self):
        return self.products.all()

    def calculate_total_price(self):
        total = 0
        order_items = OrderItem.objects.filter(order=self)
        for order_item in order_items:
            total += order_item.product.get_price() * order_item.quantity
        self.total_price = total

    def get_total_price(self):
        return self.total_price

    def get_created_at(self):
        return self.created_at


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order Item - Order #{self.order_id}, Product: {self.product.get_name()}"

    def get_order(self):
        return self.order

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity