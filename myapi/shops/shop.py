from myapi.shops.consts import domains, pages_names


class Shop:

	domain = ""
	page_names = {}

	def __init__(self, name):
		self.domain = domains[name]
		self.page_names = pages_names[name]

	def product_list_to_db(self):
		pass
