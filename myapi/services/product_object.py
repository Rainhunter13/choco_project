from myapi.repository.models import Product as ProductModel


def find_min_price(category):
	products = ProductModel.objects.all().filter(category=category)
	min_price = 1e8
	min_price_product = products.first()
	for product in products:
		cur_min_price = 1e8
		price_history = product.price_history
		price = price_history.all().last()
		for field in dir(price):
			if field.endswith('price') and cur_min_price > getattr(price, field) > 0:
				cur_min_price = getattr(price, field)
		if cur_min_price < min_price:
			min_price = cur_min_price
			min_price_product = product
	return min_price_product


def find_max_price(category):
	products = ProductModel.objects.all().filter(category=category)
	max_price = -1
	max_price_product = products.last()
	for product in products:
		cur_max_price = -1
		price_history = product.price_history
		price = price_history.all().last()
		for field in dir(price):
			if field.endswith('price') and cur_max_price < getattr(price, field):
				cur_max_price = getattr(price, field)
		if cur_max_price > max_price:
			max_price = cur_max_price
			max_price_product = product
	return max_price_product


class ProductObject:

	id = None
	name = ""
	category = ""
	sulpak_price = -1
	technodom_price = -1
	mechta_price = -1
	veter_price = -1

	def __init__(self, id, name, category, sulpak_price, technodom_price, mechta_price, veter_price):
		self.id = id
		self.name = name
		self.category = category
		self.sulpak_price = sulpak_price
		self.technodom_price = technodom_price
		self.mechta_price = mechta_price
		self.veter_price = veter_price

	def is_similar(self, product):
		return self.name == product.name

	def update_list(self, products, old_product):
		ind = 0
		for p in products:
			if p.name == old_product.name:
				new_Product = old_product
				for price_field in dir(self):
					if price_field.endswith("price") and getattr(self, price_field) >= 0:
						setattr(new_Product, price_field, getattr(self, price_field))
				products[ind] = new_Product
			ind += 1
		return products
