# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-07-16 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Género'),
        ),
    ]
