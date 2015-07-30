# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('weekly', models.BooleanField(default=True)),
                ('daily', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('avatar_url', models.CharField(verbose_name='Avatar Url', max_length=200, unique=True, blank=True, null=True)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('github_login', models.CharField(verbose_name='Login GitHub', max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('number', models.IntegerField(unique=True)),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=200, blank=True, null=True)),
                ('body', models.TextField(null=True, blank=True)),
                ('html_url', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField()),
                ('close_at', models.DateTimeField(null=True, blank=True)),
                ('update_at', models.DateTimeField()),
                ('due_on', models.DateTimeField(null=True, blank=True)),
                ('assignee', models.ForeignKey(to='journal.Developer', null=True, related_name='assignee_issues', blank=True)),
                ('closed_by', models.ForeignKey(to='journal.Developer', null=True, related_name='closedby_issues', blank=True)),
                ('creator', models.ForeignKey(to='journal.Developer', related_name='creator_issues')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField()),
                ('color', models.CharField(max_length=10, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('number', models.IntegerField(unique=True)),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=200, blank=True, null=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('html_url', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField()),
                ('close_at', models.DateTimeField(null=True, blank=True)),
                ('update_at', models.DateTimeField()),
                ('due_on', models.DateTimeField(null=True, blank=True)),
                ('creator', models.ForeignKey(to='journal.Developer', related_name='creator_milestones')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('html_url', models.TextField(null=True, blank=True)),
                ('avatar_url', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('html_url', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField()),
                ('creator', models.ForeignKey(to='journal.Developer', related_name='projects')),
            ],
        ),
        migrations.AddField(
            model_name='milestone',
            name='project',
            field=models.ForeignKey(to='journal.Project', related_name='milestones', db_column='project_id'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='sender',
            field=models.ForeignKey(to='journal.Developer', null=True, related_name='sender_miletones', blank=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='labels',
            field=models.ForeignKey(to='journal.Label', related_name='issues', db_column='label_id'),
        ),
        migrations.AddField(
            model_name='issue',
            name='milestone',
            field=models.ForeignKey(to='journal.Milestone', related_name='issues', db_column='milestone_id'),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(to='journal.Project', related_name='issues', db_column='project_id'),
        ),
        migrations.AddField(
            model_name='issue',
            name='sender',
            field=models.ForeignKey(to='journal.Developer', null=True, related_name='sender_issues', blank=True),
        ),
        migrations.AddField(
            model_name='config',
            name='manager',
            field=models.ForeignKey(to='journal.Manager'),
        ),
        migrations.AddField(
            model_name='config',
            name='projects',
            field=models.ManyToManyField(to='journal.Project', db_column='config_manager'),
        ),
    ]
