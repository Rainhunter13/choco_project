import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "choco_project.settings")
django.setup()


def test_min_price():
	from myapi.services.product_object import find_min_price
	min_price_product = find_min_price('laptop')
	min_price = 1e8
	for field in dir(min_price_product.price_history.all().first()):
		if field.endswith("price") and 0 < getattr(min_price_product.price_history.all().first(), field) < min_price:
			min_price = getattr(min_price_product.price_history.all().first(), field)
	assert min_price == 7990


def test_max_price():
	from myapi.services.product_object import find_max_price
	max_price_product = find_max_price('laptop')
	max_price = 0
	for field in dir(max_price_product.price_history.all().first()):
		if field.endswith("price") and max_price < getattr(max_price_product.price_history.all().first(), field):
			max_price = getattr(max_price_product.price_history.all().first(), field)
	assert max_price == 197890
