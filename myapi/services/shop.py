from myapi.services.consts import domains, pages_names


class Shop:

	domain = ""
	page_names = {}

	def __init__(self, name):
		self.domain = domains[name]
		self.page_names = pages_names[name]

	def parse(self, category):
		return []
