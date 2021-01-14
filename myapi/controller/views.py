from rest_framework import viewsets

from .serializers import ProductListSerializer, ProductSerializer
from myapi.repository.models import Product


# Create your views here.
class ProductListViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().order_by('category')
	serializer_class = ProductListSerializer
	http_method_names = ['get']


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().order_by('category')
	serializer_class = ProductSerializer
	lookup_field = 'id'
	http_method_names = ['get']
