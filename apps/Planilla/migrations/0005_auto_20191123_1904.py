# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-11-23 19:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Planilla', '0004_auto_20191123_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallemes',
            name='contrato',
        ),
        migrations.RemoveField(
            model_name='planilla',
            name='contrato',
        ),
        migrations.DeleteModel(
            name='DetalleMes',
        ),
        migrations.DeleteModel(
            name='Planilla',
        ),
    ]
