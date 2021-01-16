import requests
from bs4 import BeautifulSoup

from myapi.services.shop import Shop


class Veter(Shop):

	def __init__(self):
		super().__init__("veter")

	def parse(self, category):
		return []

		all_products_objects = []
		url = self.domain + self.page_names[category]

		response = requests.get(url)
		soup = BeautifulSoup(response.text)

		return all_products_objects
