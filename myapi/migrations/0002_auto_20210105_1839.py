# Generated by Django 3.1.4 on 2021-01-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=60),
        ),
    ]
