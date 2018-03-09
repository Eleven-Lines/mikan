# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-09 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20180309_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='exective_generation',
            new_name='executive_generation',
        ),
        migrations.AlterField(
            model_name='member',
            name='ja_first_name',
            field=models.CharField(blank=True, default='', max_length=16, verbose_name='Last name (ja)'),
        ),
        migrations.AlterField(
            model_name='member',
            name='ja_last_name',
            field=models.CharField(blank=True, default='', max_length=16, verbose_name='First name (ja)'),
        ),
    ]
