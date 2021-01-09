import json

from myapi.shops.shop import Shop
from myapi.shops.product_object import ProductObject


class Mechta(Shop):

	def __init__(self):
		super().__init__("mechta")

	def parse(self, category):

		all_products_objects = []
		url = self.domain + self.page_names[category]

		import requests
		response = requests.get(url)
		js = json.loads(response.text)['data']['ITEMS']
		for product in js:
			p = ProductObject(None, product['NAME'], category, -1, -1, product['PRICE']['PRICE'], -1)
			all_products_objects.append(p)

		return all_products_objects
