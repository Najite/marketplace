from django.db import models
from django.contrib.auth import get_user_model
import uuid

from products.models import Product

User = get_user_model()

# Create your models here.
class Order(models.Model):
    STATUS = (
        ("PENDING_STATE", "Pending",),
        ("COMPLETED_STATE", "Completed"),
    )
    buyer = models.ForeignKey(User,
                              related_name='order', on_delete=models.CASCADE)
    order_number = models.UUIDField(
        default=uuid.uuid4,
        
        
    )
    status = models.CharField(choices=STATUS, default='Pending', max_length=50)
    paid = models.BooleanField(default=False)
    address = models.CharField(max_length=100)
    
    
    @staticmethod
    def create_order(buyer, order_number, address, paid=False):
        order = Order()
        order.buyer = buyer
        order.order_number = order_number
        order.paid = paid
        order.save()
        return order


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_order', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    @staticmethod
    def create_order(order, product, quantity, total):
        order_item = OrderItem()
        order_item.order = order
        order_item.product = product
        order_item.quantity = quantity
        order_item.total = total
        order_item.save()
        return order_item 
    
    
    
    
    