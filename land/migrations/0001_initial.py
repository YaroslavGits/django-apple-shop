# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sabscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabscriber_name', models.CharField(max_length=200)),
                ('sabscriber_email', models.EmailField(max_length=254)),
            ],
        ),
    ]