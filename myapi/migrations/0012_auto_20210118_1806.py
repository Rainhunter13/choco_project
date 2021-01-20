# Generated by Django 3.1.5 on 2021-01-18 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0011_auto_20210118_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='myapi.product'),
        ),
    ]