from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json

from myapi.shops.shop import Shop
from myapi.requirements import chrome_version


class Sulpak(Shop):

	def __init__(self):
		super().__init__("sulpak")

	def parse(self, category):

		all_products = []
		url = self.domain + self.page_names[category] + "?page="

		page = 1
		driver = webdriver.Chrome(ChromeDriverManager(version=chrome_version).install())
		driver.get(url)
		data_total = int(driver.find_element_by_class_name("second-title-part").get_attribute("data-total"))

		while True:
			cur_url = url + str(page)
			driver.get(cur_url)
			js_vars = driver.find_elements_by_tag_name("script")

			for var in js_vars:
				text = var.get_attribute("innerHTML")
				text = text.strip()
				if text.startswith("window.insider_object") and "listing" in text:
					text = text.replace("'", '"')
					text = text[88:-52]
					products = text.split(",\n            \n                ")
					for product in products:
						all_products.append(json.loads(product))

			if len(all_products) >= data_total:
				break
			page += 1

		return all_products