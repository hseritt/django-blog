# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 18:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20171010_0607'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
