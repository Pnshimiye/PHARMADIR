# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-03 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='phone_number',
            field=models.CharField(default=3, max_length=12),
            preserve_default=False,
        ),
    ]
