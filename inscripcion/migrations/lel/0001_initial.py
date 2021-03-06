# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-02 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catequizando',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nombre_madre', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_padre', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('lugar_de_bautizo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_de_bautizo', models.DateTimeField()),
            ],
        ),
    ]
