# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usermanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_id',
            field=models.CharField(max_length=255),
        ),
    ]
