# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20170927_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('text', models.TextField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]
