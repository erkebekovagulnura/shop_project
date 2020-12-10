from rest_framework.routers import SimpleRouter
from .views import ProductsViewSet

router = SimpleRouter()
router.register(r'products', ProductsViewSet, basename="products"),
# router.register(r'product_image', ProductImageViewSet, basename="product_image")

urlpatterns = router.urls