import os
from google.cloud import bigquery

credentials_path = os.path.dirname(os.path.abspath("bigquery.py")) + "/choco-big-query-dfd0bc97cb2a.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
client = bigquery.Client()

tables = client.list_tables("choco_bq")
for table in tables:
    print("{}.{}.{}".format(table.project, table.dataset_id, table.table_id))

table_id = "choco-big-query.choco_bq.Product"

prices = {
    "sulpak" : 100900,
    "technodom": None,
    "mechta": None,
    "veter": None,
}

rows_to_insert = [
    {
        u"Title": u"Test Laptop 4",
        u"Category": u"laptop",
        u"Prices": prices,
        u"id": 600,
    }
]

errors = client.insert_rows_json(
    table_id, rows_to_insert, row_ids=[None]*len(rows_to_insert)
)

if not errors:
    print("Rows successfully added")
else:
    print(format(errors))
