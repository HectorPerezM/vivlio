# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-07-16 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.CharField(blank=True, max_length=200, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='language_code',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='original_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='small_image_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.CharField(blank=True, max_length=200, verbose_name='Resumen'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Título'),
        ),
    ]
