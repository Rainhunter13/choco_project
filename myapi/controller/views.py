from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from myapi.services.product_object import find_min_price, find_max_price
from myapi.repository.models import Product
from .serializers import ProductListSerializer, ProductSerializer


class ProductListViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().order_by('category')
	serializer_class = ProductListSerializer
	http_method_names = ['get']


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().order_by('category')
	serializer_class = ProductSerializer
	lookup_field = 'id'
	http_method_names = ['get']


class LaptopViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().filter(category='laptop')
	serializer_class = ProductListSerializer
	http_method_names = ['get']

	@action(methods=['get'], detail=True, url_path='min_price')
	def min_price(self, request, pk=None):
		product = find_min_price('laptop')
		serializer = ProductSerializer(product, many=False)
		return Response(serializer.data)

	@action(methods=['get'], detail=True, url_path='max_price')
	def max_price(self, request, pk=None):
		product = find_max_price('laptop')
		serializer = ProductSerializer(product, many=False)
		return Response(serializer.data)


class TabletViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().filter(category='tablet')
	serializer_class = ProductListSerializer
	http_method_names = ['get']

	@action(methods=['get'], detail=True, url_path='min_price')
	def min_price(self, request, pk=None):
		product = find_min_price('tablet')
		serializer = ProductSerializer(product, many=False)
		return Response(serializer.data)

	@action(methods=['get'], detail=True, url_path='max_price')
	def max_price(self, request, pk=None):
		product = find_max_price('tablet')
		serializer = ProductSerializer(product, many=False)
		return Response(serializer.data)


class MonitorViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().filter(category='monitor')
	serializer_class = ProductListSerializer
	http_method_names = ['get']

	@action(methods=['get'], detail=True, url_path='min_price')
	def min_price(self, request, pk=None):
		product = find_min_price('monitor')
		serializer = ProductSerializer(product, many=False)
		return Response(serializer.data)

	@action(methods=['get'], detail=True, url_path='max_price')
	def max_price(self, request, pk=None):
		product = find_max_price('monitor')
		serializer = ProductSerializer(product, many=False)
		return Response(serializer.data)


class EBookViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().filter(category='eBook')
	serializer_class = ProductListSerializer
	http_method_names = ['get']

	@action(methods=['get'], detail=True, url_path='min_price')
	def min_price(self, request, pk=None):
		product = find_min_price('eBook')
		serializer = ProductSerializer(product, many=False)
		return Response(serializer.data)

	@action(methods=['get'], detail=True, url_path='max_price')
	def max_price(self, request, pk=None):
		product = find_max_price('eBook')
		serializer = ProductSerializer(product, many=False)
		return Response(serializer.data)
