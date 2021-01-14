from rest_framework import serializers
from myapi.repository.models import Product, PriceHistory


class ProductListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ('category', 'id', 'name')


class PriceHistorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PriceHistory
		fields = ('date_time', 'sulpak_price', 'technodom_price', 'mechta_price', 'veter_price')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	price_history = PriceHistorySerializer(many=True)

	class Meta:
		model = Product
		fields = ['category', 'id', 'name', 'description', 'price_history']
