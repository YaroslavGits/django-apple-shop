# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-08 16:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_productinbasket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinbasket',
            old_name='product_status',
            new_name='is_active',
        ),
    ]
