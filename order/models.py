from django.db import models
from product.models import Product, Image
from django.contrib.auth.models import User

# Create your models here.

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def get_total_price(self):
        total = self.quantity * self.item.price
        return total
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)
    # shipping_address
    # billing_address
    # payment
    # coupon
    # received
    # refound_requested
    # refound_granted

    def __str__(self):
        return self.user.username

    def get_all_total(self):
        total = 0
        for item in self.items.all():
            total += item.get_total_price()
        return total