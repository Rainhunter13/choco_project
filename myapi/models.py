from django.db import models


# Create your models here.
class Product(models.Model):
	category = models.CharField(max_length=60, default="no category")
	name = models.CharField(max_length=500, default="no name")
	price = models.IntegerField(default=-1)

