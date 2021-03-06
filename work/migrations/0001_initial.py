# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-05 08:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateTimeField(null=True, verbose_name='start at')),
                ('end_at', models.DateTimeField(blank=True, null=True, verbose_name='end at')),
                ('is_just_staying', models.BooleanField(default=False, verbose_name='just staying')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('create_work_universally', 'Can create work universally'),),
            },
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='workplace name')),
                ('color', models.CharField(default='#fda313', max_length=7, verbose_name='color code(hex)')),
                ('danger', models.BooleanField(default=False, verbose_name='danger')),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='workplace',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='work.Workplace'),
        ),
    ]
