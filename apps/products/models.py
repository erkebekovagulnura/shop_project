from django.db import models

# Create your models here.
from apps.category.models import Category


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    available = models.CharField(max_length=255, verbose_name='Наличие в магазине')
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    characteristic = models.TextField(verbose_name='Характеристика', null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'products'
        verbose_name_plural = 'products'


    def __str__(self):
        return self.title

# class Review(models.Model):
#     email = models.EmailField()
#     name = models.CharField("Имя", max_length=50)
#     text = models.TextField("Сообщение", max_length=5000)
#     # parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
#     products = models.ForeignKey(Products, verbose_name="продукты", on_delete=models.CASCADE, related_name="reviews")

#     def __str__(self):
#         return f"{self.name} - {self.products}"
    
#     class Meta:
#         verbose_name = "Отзыв"
#         verbose_name_plural = "Отзывы"