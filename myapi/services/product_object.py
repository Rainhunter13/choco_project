from myapi.repository.models import Product as ProductModel


def find_min_price(category):
	products = ProductModel.objects.all().filter(category=category)
	min_price = 1e8
	min_price_product = products.last()
	min_price_shop = ""
	for product in products:
		cur_min_price = -1
		cur_shop = ""
		for price in product.prices.all():
			if price.price is not None and price.price < cur_min_price:
				cur_min_price = price.price
				cur_shop = price.seller
		if cur_min_price < min_price:
			min_price = cur_min_price
			min_price_shop = cur_shop
			min_price_product = product
	return min_price_product, min_price_shop


def find_max_price(category):
	products = ProductModel.objects.all().filter(category=category)
	max_price = -1
	max_price_product = products.last()
	max_price_shop = ""
	for product in products:
		cur_max_price = -1
		cur_shop = ""
		for price in product.prices.all():
			if price.price is not None and price.price > cur_max_price:
				cur_max_price = price.price
				cur_shop = price.seller
		if cur_max_price > max_price:
			max_price = cur_max_price
			max_price_shop = cur_shop
			max_price_product = product
	return max_price_product, max_price_shop


class ProductObject:

	id = None
	title = ""
	category = ""
	prices = {}

	def __init__(self, uid, title, category, prices):
		self.id = uid
		self.title = title
		self.category = category
		self.prices = prices

	def is_similar(self, old_product):
		return self.title == old_product.title

	def update_list(self, products, old_product):
		ind = 0
		for product in products:
			if product.name == old_product.name:
				new_product = old_product
				for shop in self.prices:
					if self.prices[shop] is not None:
						new_product.prices[shop] = self.prices[shop]
				products[ind] = new_product
			ind += 1
		return products
