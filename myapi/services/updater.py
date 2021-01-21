from datetime import datetime

from myapi.repository.models import Product as ProductModel
from myapi.repository.models import PriceRecording
from myapi.repository.models import Price

from .sulpak import Sulpak
from .technodom import Technodom
from .mechta import Mechta
from .veter import Veter
from .consts import CATEGORIES
from .consts import SHOP_CLASSES
from .consts import SHOPS


def get_new_products():
	"""Returns a list of products objects parsed from all shops and categories"""
	all_products = []
	for shop_name in SHOP_CLASSES:
		for category in CATEGORIES:
			shop_class = globals()[shop_name]
			shop = shop_class()
			products = shop.parse(category)
			for product in products:
				all_products.append(product)
	return all_products


def update_postgres():
	"""Update the Postgresql database with the list of newly parsed product objects list"""
	products = get_new_products()
	for product in products:
		same_products = ProductModel.objects.filter(title=product.title)
		if len(same_products) > 0:
			new_product = same_products.first()
		else:
			new_product = ProductModel(title=product.title, category=product.category)
			new_product.save()
		price_recording = PriceRecording(
			product=new_product,
			date_time=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		)
		price_recording.save()
		new_product.prices.clear()
		for shop in SHOPS:
			price = Price(product=new_product, price_recording=price_recording, seller=shop, price=product.prices[shop])
			price.save()


def unite_similar_products():
	"""Unite similar products into one (inside Postgres)"""
	return


def update_big_query():
	"""Update the Big Query database with the list of newly parsed product objects list"""
	import os
	from google.cloud import bigquery
	credentials_path = os.path.dirname(os.path.abspath("updater.py")) + "/choco-big-query-2-44bb243a8b97.json"
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

	schema = [
		bigquery.SchemaField("Title", "STRING", mode="NULLABLE"),
		bigquery.SchemaField("Category", "STRING", mode="NULLABLE"),
		bigquery.SchemaField(
			"Prices",
			"RECORD",
			mode="NULLABLE",
			fields=[
				bigquery.SchemaField("sulpak", "INTEGER", mode="NULLABLE"),
				bigquery.SchemaField("technodom", "INTEGER", mode="NULLABLE"),
				bigquery.SchemaField("mechta", "INTEGER", mode="NULLABLE"),
				bigquery.SchemaField("veter", "INTEGER", mode="NULLABLE"),
			]
		),
		bigquery.SchemaField("id", "INTEGER", mode="NULLABLE")
	]

	client = bigquery.Client()
	dataset_id = "choco-big-query-2.products_dataset"
	old_table_id = ""
	new_table_id = ""

	for table in client.list_tables(dataset_id):
		table_id = dataset_id + "." + table.table_id
		old_table_id = table_id
		table_id = table_id.split("__")[0]
		new_table_id = table_id + "__" + datetime.now().strftime("%d-%m-%Y--%H-%M-%S")
		break

	# DELETE OLD TABLE
	client.delete_table(old_table_id, not_found_ok=True)

	# CREATE CREATE TABLE
	new_table = bigquery.Table(new_table_id, schema)
	new_table = client.create_table(new_table)

	rows_to_insert = []
	import os
	from google.cloud import bigquery

	products = ProductModel.objects.all()
	for product in products:
		prices = {}
		for price in product.prices.all():
			prices[price.seller] = price.price
		new_row = {
			u"Title": product.title,
			u"Category": product.category,
			u"Prices": prices,
			u"id": product.id,
		}
		rows_to_insert.append(new_row)

	client.query("""
		CREATE OR REPLACE TABLE `choco-big-query.choco_bq.Product`
		AS SELECT * FROM `choco-big-query.choco_bq.Product` LIMIT 0;
	""")
	client.insert_rows_json(new_table_id, rows_to_insert, row_ids=[None]*len(rows_to_insert))
