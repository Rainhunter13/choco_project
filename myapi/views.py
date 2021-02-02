from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myapi.services.product_object import find_min_price, find_max_price
from myapi.models import Product
from .serializers import ProductListSerializer, ProductSerializer, ProductOldPricesSerializer, MinMaxSerializer


# ---------------------------------------------- PRODUCT VIEW SETS -----------------------------------------------------
class ProductListViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().order_by('id')
	serializer_class = ProductListSerializer
	http_method_names = ['get']


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().order_by('id')
	serializer_class = ProductSerializer
	lookup_field = 'id'
	http_method_names = ['get']


# ------------------------------------------------ SELLER VIEWS --------------------------------------------------------
@api_view(['GET'])
def seller_product_list(request, seller):
	serializer = ProductOldPricesSerializer(
		Product.objects.filter(old_prices__prices__seller=seller, old_prices__prices__price__gt=0).distinct(),
		many=True
	)
	return Response(serializer.data)


@api_view(['GET'])
def seller_product(request, seller, id):
	serializer = ProductOldPricesSerializer(
		Product.objects.filter(id=id),
		many=True
	)
	return Response(serializer.data)


# ----------------------------------------------- CATEGORY VIEWS -------------------------------------------------------
@api_view(['GET'])
def category(request, ctg):
	data = Product.objects.filter(category=ctg)
	serializer = ProductSerializer(data, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def category_min_price(request, ctg):
	product, seller = find_min_price(ctg)
	serializer = MinMaxSerializer(product, many=False)
	return Response(serializer.data)


@api_view(['GET'])
def category_max_price(request, ctg):
	product, seller = find_max_price(ctg)
	serializer = MinMaxSerializer(product, many=False)
	return Response(serializer.data)
