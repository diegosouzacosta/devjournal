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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('weekly', models.BooleanField(default=True)),
                ('daily', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('avatar_url', models.CharField(max_length=200, blank=True, null=True, verbose_name='Avatar Url', unique=True)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('github_login', models.CharField(max_length=100, verbose_name='Login GitHub', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('number', models.IntegerField(unique=True)),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=200, blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('html_url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('close_at', models.DateTimeField(blank=True, null=True)),
                ('update_at', models.DateTimeField()),
                ('due_on', models.DateTimeField(blank=True, null=True)),
                ('assignee', models.ForeignKey(blank=True, related_name='assignee_issues', null=True, to='journal.Developer')),
                ('closed_by', models.ForeignKey(blank=True, related_name='closedby_issues', null=True, to='journal.Developer')),
                ('creator', models.ForeignKey(to='journal.Developer', related_name='creator_issues')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('color', models.CharField(max_length=10, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('number', models.IntegerField(unique=True)),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=200, blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('html_url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('close_at', models.DateTimeField(blank=True, null=True)),
                ('update_at', models.DateTimeField()),
                ('due_on', models.DateTimeField(blank=True, null=True)),
                ('creator', models.ForeignKey(to='journal.Developer', related_name='creator_milestones')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('html_url', models.TextField(blank=True, null=True)),
                ('avatar_url', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('html_url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('creator', models.ForeignKey(to='journal.Developer', related_name='projects')),
                ('organization', models.ForeignKey(to='journal.Organization', related_name='projects')),
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
            field=models.ForeignKey(blank=True, related_name='sender_miletones', null=True, to='journal.Developer'),
        ),
        migrations.AddField(
            model_name='manager',
            name='organization',
            field=models.ForeignKey(to='journal.Organization', related_name='journal_manager'),
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
            field=models.ForeignKey(blank=True, related_name='sender_issues', null=True, to='journal.Developer'),
        ),
        migrations.AddField(
            model_name='developer',
            name='organization',
            field=models.ForeignKey(to='journal.Organization', related_name='journal_developer'),
        ),
        migrations.AddField(
            model_name='config',
            name='manager',
            field=models.ForeignKey(to='journal.Manager'),
        ),
        migrations.AddField(
            model_name='config',
            name='projects',
            field=models.ManyToManyField(db_column='config_manager', to='journal.Project'),
        ),
    ]
