# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-14 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(blank=True, max_length=192, verbose_name='Title'),
        ),
    ]
