# Generated by Django 3.1.5 on 2021-01-17 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0009_auto_20210110_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricehistory',
            name='mechta_price',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='pricehistory',
            name='sulpak_price',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='pricehistory',
            name='technodom_price',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='pricehistory',
            name='veter_price',
            field=models.IntegerField(default=-1),
        ),
    ]
