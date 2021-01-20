# NEXT 4 LINES ARE ONLY FOR DIRECT TESTING:
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "choco_project.settings")
# django.setup()

import requests
import json
from bs4 import BeautifulSoup

from myapi.services.seller import Seller
from myapi.services.product_object import ProductObject
from myapi.services.consts import SHOPS


class Veter(Seller):

	def __init__(self):
		super().__init__("veter")

	def parse(self, category):
		# return []

		all_products_objects = []
		url = self.domain + self.page_names[category] + "?PAGEN_1="

		current_url = url + "1"
		response = requests.get(url=current_url, headers={
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
			'(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
		})

		soup = BeautifulSoup(response.text, 'html.parser')
		div_tot = soup.find("div", class_="bx_catalog_sort_block")
		tot_products = int(div_tot.span.strong.text)

		page = 1
		while True:

			current_url = url + str(page)
			response = requests.get(url=current_url, headers={
				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
				'(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
			})

			soup = BeautifulSoup(response.text, 'html.parser')
			script_tags = soup.findAll("script")
			for script_tag in script_tags:
				if str(script_tag.string).startswith("\nvar obbx_"):
					script_string = str(script_tag.string)
					script_string = script_string.strip()
					script_string = script_string.split("JCCatalogSectionExtend(")[1][0:-2]
					script_string = script_string.replace("'", '"')
					product_json = json.loads(script_string)
					name = product_json['PRODUCT']['NAME']
					price = product_json['PRODUCT']['BASIS_PRICE']['VALUE']
					prices = {}
					for shop in SHOPS:
						prices[shop] = None
					prices['veter'] = price
					product_object = ProductObject(None, name, category, prices)
					all_products_objects.append(product_object)

			if len(all_products_objects) >= tot_products:
				break
			page += 1

		return all_products_objects

# TESTING PARSER:
# s = Veter()
# ps = s.parse("laptop")
# for p in ps:
# 	print(str(p.title) + " " + str(p.prices["veter"]) + " " + str(p.prices["mechta"]))
