# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-13 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tag',
            field=models.ManyToManyField(blank=True, to='tags.TagAffinity', verbose_name='Affinidad'),
        ),
    ]
