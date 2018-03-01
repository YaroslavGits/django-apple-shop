# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-02 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_remove_productinorder_delivery_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
