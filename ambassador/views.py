from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Product
from .serializers import ProductSerializer
from django.core.cache import cache
import time

# Create your views here.


class ProductFrontEndAPIView(APIView):
    @method_decorator(cache_page(60*60*2, key_prefix='products_frontend'))
    def get(self, __):
        time.sleep(2)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductBackendEndAPIView(APIView):
    def get(self, __):
        products = cache.get('products_backend')
        if not products:
            time.sleep(2)
            products = list(Product.objects.all())
            cache.set('products_backend', products, timeout=60*30)  # 30minº
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
