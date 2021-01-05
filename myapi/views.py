from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ProductSerializer
from .models import Product


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().order_by('name')
	serializer_class = ProductSerializer
