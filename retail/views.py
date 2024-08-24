from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter

from retail.models import RetailChain, Product
from retail.serializers import RetailChainSerializer, ProductSerializer


class RetailChainViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RetailChainSerializer
    queryset = RetailChain.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["country"]

    def perform_update(self, serializer):
        if 'debt' in serializer.validated_data:
            serializer.validated_data.pop('debt')
        super().perform_update(serializer)


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
