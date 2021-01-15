from myapi.services.consts import DOMAINS, PAGES_NAMES


class Shop:

	domain = ""
	page_names = {}

	def __init__(self, name):
		self.domain = DOMAINS[name]
		self.page_names = PAGES_NAMES[name]

	def parse(self, category):
		return []
