from django.test import TestCase


# Create your tests here.
# def test_product_endpoint_get():
# 	import requests
# 	response = requests.get("http://localhost:8000/product/")
# 	print(response.text)
# 	assert 1 == 1


def test_sulpak():
	from myapi.shops.sulpak import Sulpak
	sulpak = Sulpak()
	all_products = sulpak.parse("laptop")
	print(all_products)
	assert len(all_products) == 359
