# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-07-16 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20200716_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.CharField(blank=True, max_length=10000, null=True, verbose_name='Resumen'),
        ),
    ]
