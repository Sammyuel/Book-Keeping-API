# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-20 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_odds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odds',
            name='odds',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
    ]
