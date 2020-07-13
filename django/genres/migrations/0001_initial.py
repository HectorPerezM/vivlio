# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-07-12 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_remove_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20, unique=True, verbose_name='genre')),
                ('user', models.ManyToManyField(null=True, to='users.User', verbose_name='Usuario')),
            ],
        ),
    ]