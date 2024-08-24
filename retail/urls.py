from rest_framework.routers import DefaultRouter

from retail.apps import RetailConfig
from retail.views import RetailChainViewSet, ProductViewSet

app_name = RetailConfig.name

router = DefaultRouter()
router.register(r'retail_chains', RetailChainViewSet, basename='retail_chains')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [] + router.urls
