# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0017_auto_20180107_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='status_test',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
