from rest_framework.routers import SimpleRouter
from .views import ProductsViewSet

router = SimpleRouter()
router.register(r'products', ProductsViewSet, basename='products')

urlpatterns = router.urls