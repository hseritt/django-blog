# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendedlink',
            name='url',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='sitelink',
            name='url',
            field=models.TextField(unique=True),
        ),
    ]
