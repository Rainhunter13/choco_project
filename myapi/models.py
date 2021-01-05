from django.db import models


# Create your models here.
class Product(models.Model):
	category = models.CharField(max_length=60, default="")
	name = models.CharField(max_length=60, default="")

	def __str__(self):
		return self.name
