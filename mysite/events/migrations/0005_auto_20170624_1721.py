# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-24 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_titles_profit'),
        ('events', '0004_auto_20170620_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('players', models.CharField(max_length=100)),
                ('titles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Titles')),
            ],
        ),
        migrations.AlterField(
            model_name='odds',
            name='titles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Titles'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='titles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Titles'),
        ),
    ]
