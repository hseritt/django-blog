# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20170930_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('content', markdownx.models.MarkdownxField()),
                ('is_visible', models.BooleanField(default=False)),
            ],
        ),
    ]
