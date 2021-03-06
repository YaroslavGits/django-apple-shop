# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-04 01:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20180104_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusdelivery',
            name='delivery',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Delivery'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='price_for_delivery_type',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
