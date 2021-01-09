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
