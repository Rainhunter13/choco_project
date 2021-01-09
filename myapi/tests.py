from django.test import TestCase
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "choco_project.settings")
django.setup()


def test_product_list_endpoint():
	import requests
	response = requests.get("http://localhost:8000/product/")
	assert response.status_code < 300


def test_product_endpoint():
	import requests
	response = requests.get("http://localhost:8000/product/42/")
	assert response.text.__contains__("sulpak_price")


def test_sulpak():
	from myapi.shops.sulpak import Sulpak
	sulpak = Sulpak()
	all_products = sulpak.parse("laptop")
	print(len(all_products))
	print(all_products)
	assert len(all_products) > 0


def test_save_to_db():
	from myapi.models import PriceHistory
	from myapi.models import Product as ProductModel
	from datetime import datetime
	product = ProductModel(name="HP Laptop", category="laptop")
	product.save()
	price = PriceHistory(
		product=product,
		date_time=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
		sulpak_price=277900,
		technodom_price=259900,
		mechta_price=260000,
		veter_price=299000
	)
	price.save()
	assert 1 == 1


def test_updater():
	from myapi.shops.updator import Updater
	u = Updater()
	u.update_db()


test_updater()
