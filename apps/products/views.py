from django.shortcuts import render
from rest_framework import viewsets, permissions
# from django.db.models import Q
from rest_framework.filters import SearchFilter
# from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination


from apps.products.serializers import ProductsSerializer


from .models import  Products




class ProductsPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 20


# class ProductsViewSet(viewsets.ModelViewSet):
#     serializer_class = ProductsSerializer
#     queryset = Products.objects.all()
#     permission_class = (permissions.IsAuthenticated)
#     paginator = ProductsPagination()
#     filter_backends = [SearchFilter]
#     search_fields = ['price', 'title', 'available']

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    paginator = ProductsPagination()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title', 'category']

    # def get_serializer_context(self):
    #     return {'request': self.request}


# class ProductViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get_serializer_context(self):
#         return {'request': self.request}


# class ProductImageViewSet(viewsets.ModelViewSet):
#     queryset = ProductImage.objects.all()
#     serializer_class = ProductImageSerializer

#     def get_serializer_context(self):
#         return {'request': self.request}


    # def get_queryset(self):
    #     return Products.objects.filter(
    #         author=self.request.user
    #     )

    
    # @action(detail=False, methods=['get'])           # /search/?q=hello
    # def search(self, request, pk=None):
    #     q = request.query_params.get('q')
    #     queryset = self.get_queryset()
    #     queryset = queryset.filter(Q(title__icontains=q) |
    #                                Q(description__icontains=q))
    #     serializer = ProductsSerializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def get_queryset(self):
    #     price = self.request.query_params.get('price')
    #     price_from, price_to = price.split('-')
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(price__gt=price_from,
    #                                price__lt=price_to)
    #     return queryset


    # @action(detail=False, methods=['get'])
    # def search(self, request, pk=None):
    #     q = request.query_params.get('q')
    #     queryset = self.get_queryset()


    
