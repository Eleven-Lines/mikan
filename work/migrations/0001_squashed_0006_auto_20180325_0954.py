# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-25 00:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('work', '0001_initial'), ('work', '0002_auto_20180324_1723'), ('work', '0003_work_workplan_workplanmanager'), ('work', '0004_auto_20180325_0859'), ('work', '0005_auto_20180325_0946'), ('work', '0006_auto_20180325_0954')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0007_auto_20180319_1652'),
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
        migrations.RenameModel(
            old_name='Work',
            new_name='Activity',
        ),
        migrations.AlterModelOptions(
            name='activity',
            options={'permissions': (('create_activities_universally', 'Can create activities universally'),)},
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='work name')),
                ('description', models.TextField(blank=True, help_text='Brief description for work.')),
                ('work_manual_url', models.URLField(blank=True, help_text='Wiki page for work manual.')),
                ('assigned_section', models.ManyToManyField(blank=True, help_text='Section(s) to assign this work. More than one teams or sections should be assigned.', to='members.Section')),
                ('assigned_team', models.ManyToManyField(blank=True, help_text='Team(s) to assign this work. More than one teams or sections should be assigned.', to='members.Team')),
                ('default_workplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.Workplace')),
            ],
        ),
        migrations.CreateModel(
            name='WorkPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('assigned_section', models.ManyToManyField(blank=True, help_text='Section(s) to assign this work plan.If no team or section is assigned, default of each works will be used.', to='members.Section')),
                ('assigned_team', models.ManyToManyField(blank=True, help_text='Team(s) to assign this work plan. If no team or section is assigned, default of each works will be used.', to='members.Team')),
                ('completed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workplan_completed', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, help_text='Member(s) to work on this work plan.If no member is assigned, all members in assigned teams or sections will be used.', related_name='workplan_assigned', to=settings.AUTH_USER_MODEL)),
                ('workplaces', models.ManyToManyField(blank=True, help_text='Workplace(s) for this work plan.If no workplace is assigned, default of each works will be used.', to='work.Workplace')),
            ],
        ),
        migrations.CreateModel(
            name='PracticalWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Work')),
                ('workplace', models.ForeignKey(blank=True, help_text='Change this to override default workplace. Leave it blank to use default.', null=True, on_delete=django.db.models.deletion.CASCADE, to='work.Workplace')),
                ('workplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.WorkPlan')),
            ],
        ),
        migrations.AddField(
            model_name='workplan',
            name='work',
            field=models.ManyToManyField(help_text='Work to execture in this work plan. Required.', through='work.PracticalWork', to='work.Work'),
        ),
        migrations.AlterField(
            model_name='workplan',
            name='assigned_section',
            field=models.ManyToManyField(blank=True, help_text='Section(s) to assign this work plan.If no team or section is assigned, default of each work will be used.', to='members.Section'),
        ),
        migrations.AlterField(
            model_name='workplan',
            name='assigned_team',
            field=models.ManyToManyField(blank=True, help_text='Team(s) to assign this work plan. If no team or section is assigned, default of each work will be used.', to='members.Team'),
        ),
        migrations.AlterField(
            model_name='workplan',
            name='workplaces',
            field=models.ManyToManyField(blank=True, help_text='Workplace(s) for this work plan.If no workplace is assigned, default of each work will be used.', to='work.Workplace'),
        ),
    ]
