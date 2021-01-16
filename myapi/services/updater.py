from datetime import datetime
from myapi.repository.models import PriceHistory
from myapi.repository.models import Product as ProductModel
from .sulpak import Sulpak
from .technodom import Technodom
from .mechta import Mechta
from .veter import Veter


class Updater:

	def get_all_products(self):
		all_products = []
		# for shop_name in ['Sulpak', 'Technodom', 'Mechta', 'Veter']:
		for shop_name in ['Mechta']:
			for category in ['laptop', 'tablet', 'monitor', 'eBook']:
				shop_class = globals()[shop_name]
				shop = shop_class()
				products = shop.parse(category)
				for product in products:
					exist_similar = False
					for p in all_products:
						if product.is_similar(p):
							product.update_list(all_products, p)
							exist_similar = True
					if not exist_similar:
						all_products.append(product)
		return all_products

	def update_products(self):
		products = self.get_all_products()
		for p in products:
			same_products = ProductModel.objects.all().filter(name=p.name)
			if len(same_products) > 0:
				product = same_products[0]
			else:
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
