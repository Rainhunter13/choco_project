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
				p[ind] = new_Product
			ind += 1
		return products
