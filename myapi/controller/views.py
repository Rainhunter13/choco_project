from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myapi.services.product_object import find_min_price, find_max_price
from myapi.repository.models import Product
from .serializers import ProductListSerializer, ProductSerializer, ProductOldPricesSerializer, MinMaxSerializer


class ProductListViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().order_by('id')
	serializer_class = ProductListSerializer
	http_method_names = ['get']


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().order_by('id')
	serializer_class = ProductSerializer
	lookup_field = 'id'
	http_method_names = ['get']


# ---------------------------------------------- SELLER VIEW SETS ------------------------------------------------------
class SulpakViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.filter(old_prices__prices__seller="sulpak", old_prices__prices__price__gt=0).distinct()
	serializer_class = ProductOldPricesSerializer
	lookup_field = 'id'
	http_method_names = ['get']


class TechnodomViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.filter(old_prices__prices__seller="technodom", old_prices__prices__price__gt=0).distinct()
	serializer_class = ProductOldPricesSerializer
	lookup_field = 'id'
	http_method_names = ['get']


class MechtaViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.filter(old_prices__prices__seller="mechta", old_prices__prices__price__gt=0).distinct()
	serializer_class = ProductOldPricesSerializer
	lookup_field = 'id'
	http_method_names = ['get']


class ShopViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.filter(old_prices__prices__seller="shop", old_prices__prices__price__gt=0).distinct()
	serializer_class = ProductOldPricesSerializer
	lookup_field = 'id'
	http_method_names = ['get']


# --------------------------------------------- CATEGORY VIEWS --------------------------------------------------------
@api_view(['GET'])
def category(request, cat):
	data = Product.objects.filter(category=cat)
	serializer = ProductSerializer(data, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def category_min_price(request, cat):
	product, seller = find_min_price(cat)
	serializer = MinMaxSerializer(product, many=False)
	return Response(serializer.data)


@api_view(['GET'])
def category_max_price(request, cat):
	product, seller = find_max_price(cat)
	serializer = MinMaxSerializer(product, many=False)
	return Response(serializer.data)
