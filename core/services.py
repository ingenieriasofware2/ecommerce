from domain.models import User, Category, Product, Order, OrderItem
from domain.repositories import UserRepository 


class UserService:
    
    def __init__(self, UserRepository):
        self.user_repository = UserRepository
    
    #SERVICIOS DE USER
    def create_user(self, username, email, password):
        
        return self.user_repository.create_user(username, email, password)

    def get_user_by_username(self, username):
        return self.user_repository.get_user_by_username(username)

    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)

    def update_user_password(self, username, new_password):
        user = self.user_repository.get_user_by_username(username)
        if user:
            user.password = new_password
            return self.user_repository.update_user_password(user)
        return False

    def delete_user(self, username):
        user = self.user_repository.get_user_by_username(username)
        if user:
            return self.user_repository.delete_user(user)
        return False

#servicios de category
def create_category(name, description, category_repository):
    category = category_repository.create_category(name, description)
    return category

def get_category_by_name(name, category_repository):
    return category_repository.get_category_by_name(name)

def get_category_description_by_name(name, category_repository):
    category = category_repository.get_category_by_name(name)
    if category:
        return category.get_description()
    return None

# ProductService 
def create_product(name, description, price, category, product_repository):
    return product_repository.create_product(name, description, price, category)

def get_product_id_by_name(name, product_repository):
    return product_repository.get_product_id_by_name(name)

def get_product_by_id(product_id, product_repository):
    return product_repository.get_product_by_id(product_id)

def update_product_price(product_id, new_price, product_repository):
    product = product_repository.get_product_by_id(product_id)
    if product:
        product.price = new_price
        return product_repository.update_product_price(product)
    return False


def delete_product(product_id, product_repository):
    product = product_repository.get_product_by_id(product_id)
    if product:
        return product_repository.delete_product(product)
    return False

# OrderService
def create_order(user, products, total_price):
    order = Order(user=user, total_price=total_price)
    order.save()
    
    for product, quantity in products:
        order_item = OrderItem(order=order, product=product, quantity=quantity)
        order_item.save()
    
    return order

def get_order_by_id(order_id):
    try:
        order = Order.objects.get(id=order_id)
        return order
    except Order.DoesNotExist:
        return None

def get_orders_by_user(user):
    orders = Order.objects.filter(user=user)
    return orders

def update_order_total_price(order_id, new_total_price):
    order = get_order_by_id(order_id)
    if order:
        order.total_price = new_total_price
        order.save()
        return True
    return False

def delete_order(order_id):
    order = get_order_by_id(order_id)
    if order:
        order.delete()
        return True
    return False


