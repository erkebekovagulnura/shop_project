from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination


from apps.products.serializers import ProductsSerializer
from .models import  Products



class ProductsPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 20


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    paginator = ProductsPagination()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title', 'available']
    
