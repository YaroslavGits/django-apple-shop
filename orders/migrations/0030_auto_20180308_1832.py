# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-08 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0029_auto_20180225_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='price_all',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='price_for_one',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='price_all',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='price_for_one',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
