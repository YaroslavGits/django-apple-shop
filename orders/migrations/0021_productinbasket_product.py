# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-09 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productimage_is_main'),
        ('orders', '0020_auto_20180209_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
