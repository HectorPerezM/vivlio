# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-13 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20200716_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='affinity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]