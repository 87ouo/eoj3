# Generated by Django 2.1.3 on 2019-01-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polygon', '0015_auto_20190112_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='codeforcespackage',
            name='size',
            field=models.FloatField(null=True),
        ),
    ]