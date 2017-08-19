# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothes',
            old_name='price',
            new_name='price_in_cents',
        ),
        migrations.AddField(
            model_name='clothes',
            name='internal_description',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
