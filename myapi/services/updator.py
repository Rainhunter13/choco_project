from myapi.services.sulpak import Sulpak
from myapi.services.technodom import Technodom
from myapi.services.mechta import Mechta
from myapi.services.veter import Veter
from myapi.repository.models import PriceHistory
from myapi.repository.models import Product as ProductModel
from datetime import datetime


class Updater:

	def combine_products(self):
		products_combined = []
		for shop_name in ['sulpak', 'technodom', 'mechta', 'veter']:
			for category in ['laptop', 'tablet', 'monitor', 'eBook']:
				shop = Sulpak()
				if shop_name == "technodom":
					shop = Technodom()
				if shop_name == "mechta":
					shop = Mechta()
				if shop_name == "veter":
					shop = Veter()
				products = shop.parse(category)
				for product in products:
					# update products_combined with new params if product is already there or add else
					# for now, assuming no two have same name
					products_combined.append(product)
		return products_combined

	def update_db(self):
		products = self.combine_products()
		for p in products:
			# add checker for already existing product -> would do put instead of post then!
			# for now just
			product = ProductModel(name=p.name, category=p.category)
			product.save()
			price = PriceHistory(
				product=product,
				date_time=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
				sulpak_price=p.sulpak_price,
				technodom_price=p.technodom_price,
				mechta_price=p.mechta_price,
				veter_price=p.veter_price
			)
			price.save()
		return
