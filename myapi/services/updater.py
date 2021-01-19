from datetime import datetime

from myapi.repository.models import Product as ProductModel
from myapi.repository.models import PriceRecording
from myapi.repository.models import Price

from .sulpak import Sulpak
from .technodom import Technodom
from .mechta import Mechta
from .veter import Veter
from .consts import CATEGORIES
from .consts import SHOP_CLASSES
from .consts import SHOPS


def get_all_products():
	"""Returns a list of products objects parsed from all shops and categories"""
	all_products = []
	for shop_name in SHOP_CLASSES:
		for category in CATEGORIES:
			shop_class = globals()[shop_name]
			shop = shop_class()
			products = shop.parse(category)
			for product in products:
				exist_similar = False
				for old_product in all_products:
					if product.is_similar(old_product):
						all_products = product.update_list(all_products, old_product)
						exist_similar = True
				if not exist_similar:
					all_products.append(product)
	return all_products


def update_products():
	"""Update the database with the list of newly parsed product objects list"""
	products = get_all_products()
	for product in products:
		same_products = ProductModel.objects.all().filter(title=product.title)
		if len(same_products) > 0:
			new_product = same_products[0]
		else:
			new_product = ProductModel(title=product.title, category=product.category)
			new_product.save()
		price_recording = PriceRecording(
			product=new_product,
			date_time=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		)
		price_recording.save()
		new_product.prices.clear()
		for shop in SHOPS:
			price = Price(product=new_product, price_recording=price_recording, seller=shop, price=product.prices[shop])
			price.save()
