from rest_framework.serializers import ModelSerializer

from retail.models import RetailChain, Product


class RetailChainSerializer(ModelSerializer):

    class Meta:
        model = RetailChain
        exclude = ['debt']


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
