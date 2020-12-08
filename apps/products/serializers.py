from rest_framework import serializers
from .models import Products
from apps.category.models import Category


# class ReviewCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review 
#         fields = '__all__'



class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    title = serializers.CharField(required=True)
    available = serializers.CharField(max_length=255)    
    image = serializers.ImageField(required=True)
    description = serializers.CharField(required=False)
    сharacteristic = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=20, decimal_places=2, required=True)
    
    class Meta:
        model = Products
        fields = (
            '__all__'
        )