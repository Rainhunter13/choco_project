import os
import django
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
	from .sulpak import Sulpak
	sulpak = Sulpak()
	all_products = sulpak.parse("laptop")
	assert all_products


def test_mechta():
	from .mechta import Mechta
	mechta = Mechta()
	all_products = mechta.parse("laptop")
	print(len(all_products))
	print(all_products)
	assert all_products
