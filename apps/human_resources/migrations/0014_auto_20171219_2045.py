# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0013_auto_20171219_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnelinformation',
            name='working_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='human_resources.WorkingPlace', verbose_name='务工地点'),
        ),
    ]
