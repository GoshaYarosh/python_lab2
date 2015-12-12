# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pheonix', '0002_auto_20151208_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='view',
            field=models.CharField(choices=[('info', 'Information'), ('alert', 'Alert'), ('warning', 'Warning'), ('success', 'Success')], default='info', max_length=8),
        ),
    ]