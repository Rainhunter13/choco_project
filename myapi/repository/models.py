from django.db import models


# Create your models here.
class Product(models.Model):

	title = models.CharField(max_length=500, default="N/A")
	category = models.CharField(max_length=200, default="N/A")


class PriceRecording(models.Model):
	product = models.ForeignKey(Product, related_name="old_prices", on_delete=models.CASCADE)

	date_time = models.CharField(max_length=100, default="dd.mm.yy hh:mm:ss")


class Price(models.Model):
	price_recording = models.ForeignKey(PriceRecording, related_name="prices", on_delete=models.CASCADE, null=True)
	product = models.ForeignKey(Product, related_name="prices", on_delete=models.CASCADE, null=True)

	seller = models.CharField(max_length=100)
	price = models.IntegerField(default=None, null=True)
