from django.db import models
from django.contrib.auth.models import User
from store_products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderdate = models.DateTimeField()
    shippingdate = models.DateTimeField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=7)

    def __str__(self):
        return self.orderdate.strftime("%b. %d, %Y, %I:%M %p")

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.item.name
