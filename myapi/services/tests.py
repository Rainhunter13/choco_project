import os
import django

# TO RUN THE FILE SEPARATELY FROM DJANGO APP OR PYTEST UNCOMMENT:
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "choco_project.settings")
# django.setup()


def test_product_list_endpoint():
	import requests
	response = requests.get("http://127.0.0.1:8000/product/")
	assert response.status_code < 300


def test_product_endpoint():
	import requests
	response = requests.get("http://127.0.0.1:8000/product/350/")
	assert response.text.__contains__("sulpak_price")


def test_sulpak():
	from .sulpak import Sulpak
	sulpak = Sulpak()
	all_products = sulpak.parse("laptop")
	assert all_products


def test_mechta():
	from .mechta import Mechta
	mechta = Mechta()
	all_products = mechta.parse("laptop")
	assert all_products


def test_min_price():
	from .product_object import find_min_price
	min_price_product = find_min_price('eBook')
	min_price = 1e8
	for field in dir(min_price_product.price_history.all().first()):
		if field.endswith("price") and 0 < getattr(min_price_product.price_history.all().first(), field) < min_price:
			min_price = getattr(min_price_product.price_history.all().first(), field)
	assert min_price == 7990


def test_max_price():
	from .product_object import find_max_price
	max_price_product = find_max_price('eBook')
	max_price = 0
	for field in dir(max_price_product.price_history.all().first()):
		if field.endswith("price") and max_price < getattr(max_price_product.price_history.all().first(), field):
			max_price = getattr(max_price_product.price_history.all().first(), field)
	assert max_price == 197890
