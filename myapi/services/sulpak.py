from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

from myapi.services.seller import Seller
from myapi.services.product_object import ProductObject
from myapi.services.consts import SHOPS


class Sulpak(Seller):

    def __init__(self):
        super().__init__("sulpak")

    def parse(self, category):

        # TEMPORARY -> BUG IN DOCKER & CHROMEDRIVER -> TO FIX !!!
        return []

        all_products = []
        if category not in self.page_names:
            return all_products
        url = self.domain + self.page_names[category] + "?page="

        page = 1

        driver = webdriver.Remote('http://hub:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

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

        all_products_objects = []
        for product in all_products:
            prices = {}
            for shop in SHOPS:
                prices[shop] = None
            prices['sulpak'] = product["unit_price"]
            product_object = ProductObject(None, product["name"], category, prices)
            all_products_objects.append(product_object)

        return all_products_objects
