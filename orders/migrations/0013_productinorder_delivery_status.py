# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_remove_productinorder_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='delivery_status',
            field=models.BooleanField(default=True),
        ),
    ]
