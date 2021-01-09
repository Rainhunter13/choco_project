from django.db import models


# Create your models here.
class Product(models.Model):
	category = models.CharField(max_length=60, default="no category")
	name = models.CharField(max_length=500, default="no name")

	description = models.CharField(max_length=1000, default="no description")


class PriceHistory(models.Model):
	product = models.ForeignKey(Product, related_name="price_history", on_delete=models.CASCADE)
	date_time = models.CharField(max_length=100, default="01.01.1991-00:00:00")

	sulpak_price = models.IntegerField(default=-1)
	technodom_price = models.IntegerField(default=-1)
	mechta_price = models.IntegerField(default=-1)
	veter_price = models.IntegerField(default=-1)
