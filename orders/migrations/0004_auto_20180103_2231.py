# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180103_2211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Selected Product', 'verbose_name_plural': 'Selected Products'},
        ),
        migrations.RenameField(
            model_name='delivery',
            old_name='price_for_delivery',
            new_name='price_for_delivery_type',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='delivery_status',
        ),
        migrations.AddField(
            model_name='delivery',
            name='delivery_type',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='delivery',
            name='status_delivery_type',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='statusdelivery',
            name='order',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
    ]