# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-14 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='profit',
            field=models.BigIntegerField(default=0),
        ),
    ]
