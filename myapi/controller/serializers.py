from rest_framework import serializers
from myapi.repository.models import Product, PriceRecording, Price


class PriceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Price
		fields = ('seller', 'price')


class PriceRecordingSerializer(serializers.HyperlinkedModelSerializer):
	prices = PriceSerializer(many=True)

	class Meta:
		model = PriceRecording
		fields = ('date_time', 'prices')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	prices = PriceSerializer(many=True)

	class Meta:
		model = Product
		fields = ('title', 'prices')


class ProductOldPricesSerializer(serializers.HyperlinkedModelSerializer):
	prices = PriceSerializer(many=True)
	old_prices = PriceRecordingSerializer(many=True)

	class Meta:
		model = Product
		fields = ('id', 'title', 'prices', 'old_prices')


class ProductListSerializer(serializers.HyperlinkedModelSerializer):
	prices = PriceSerializer(many=True)

	class Meta:
		model = Product
		fields = ('id', 'title', 'prices')


class MinMaxSerializer(serializers.HyperlinkedModelSerializer):
	prices = PriceSerializer(many=True)

	class Meta:
		model = Product
		fields = ('category', 'title', 'prices')
