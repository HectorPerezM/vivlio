# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-07-16 00:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=200, verbose_name='Texto')),
                ('stars', models.IntegerField(blank=True, choices=[(1, 'Muy malo'), (2, 'Malo'), (3, 'Normal'), (4, 'Bueno'), (5, 'Muy bueno')], null=True, verbose_name='Valoración')),
                ('book', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='Libro')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='Autor de la reseña')),
            ],
        ),
    ]
