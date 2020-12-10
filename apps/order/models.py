# from django.db import models

# Create your models here.
# from django.contrib.auth import get_user_model
# from django.db import models

# from apps.products.models import Products


# class OrderItem(models.Model):
#     products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='order_items')
#     quantity = models.PositiveIntegerField(default=1)
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='order_items')


# class Order(models.Model):
#     items = models.ManyToManyField('OrderItem')
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
#     created_at = models.DateTimeField(auto_now_add=True)
#     ordered_at = models.DateTimeField()


from django.db import models

from apps.products.models import Products
from apps.accounts.models import User


class Order(models.Model):
    product = models.ManyToManyField(Products, related_name='products')
    first_name = models.CharField(max_length=50, default='SOME STRING')
    last_name = models.CharField(max_length=50, default='SOME STRING')
    address = models.CharField(max_length=250, default='SOME STRING')
    city = models.CharField(max_length=100,  default='SOME STRING')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
   

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.value * self.qty