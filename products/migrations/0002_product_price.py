# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
