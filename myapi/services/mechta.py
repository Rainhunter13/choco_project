import json

from myapi.services.seller import Seller
from myapi.services.product_object import ProductObject
from .consts import SHOPS


class Mechta(Seller):

	def __init__(self):
		super().__init__("mechta")

	def parse(self, category):

		all_products_objects = []
		url = self.domain + self.page_names[category]

		import requests
		response = requests.get(url)
		js = json.loads(response.text)['data']['ITEMS']
		for product in js:
			prices = {}
			for shop in SHOPS:
				prices[shop] = None
			prices['mechta'] = product['PRICE']['PRICE']
			p = ProductObject(None, product['NAME'], category, prices)
			all_products_objects.append(p)

		return all_products_objects
