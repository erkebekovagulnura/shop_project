# from rest_framework.routers import SimpleRouter
# from .views import OrderViewSet

# router = SimpleRouter()
# # router.register(r'products', ProductsViewSet, basename="products"),
# router.register(r'order', OrderViewSet, basename="order")

# urlpatterns = router.urls


from django.urls import path

from . import views

urlpatterns = [
    path('create-order/', views.OrderCreateAPIView.as_view()),
    path('order/<int:pk>/', views.OrderDetailAPIView.as_view()),
    path('my_orders/', views.OrderAuthorListAPIView.as_view()),
]