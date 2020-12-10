from rest_framework import serializers
from .models import Products
from apps.category.models import Category



# class ReviewCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review 
#         fields = '__all__'



# class ProductsSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # title = serializers.CharField(required=False)
    # available = serializers.CharField(max_length=255)    
    # image = serializers.ImageField(required=True)
    # description = serializers.CharField(required=False)
    # сharacteristic = serializers.CharField(required=False)
    # price = serializers.DecimalField(max_digits=20, decimal_places=2, required=True)
    
    # class Meta:
    #     model = Products
    #     fields = (
    #         'category', 'title', 'description', 'available', 'price'
    #     )

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

    

# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = '__all__'

#     def _get_image_url(self, obj):
#         if obj.image:
#             url = obj.image.url
#             request = self.request.get('request')
#             if request is not None:
#                 url = request.build_absolute_uri(url)
#         else:
#             url = ''
#         return url

#     def to_representation(self, instance):
#         representation = super(ProductImageSerializer, self).to_representation(instance)
#         representation['image'] = self._get_image_url(instance)
#         return representation