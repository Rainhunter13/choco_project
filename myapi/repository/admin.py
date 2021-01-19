from django.contrib import admin
from .models import Product, PriceRecording, Price

# Register your models here.
admin.site.register(Product)
admin.site.register(PriceRecording)
admin.site.register(Price)
