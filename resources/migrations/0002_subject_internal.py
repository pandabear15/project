# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='internal',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]