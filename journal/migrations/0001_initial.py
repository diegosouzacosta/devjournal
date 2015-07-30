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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('weekly', models.BooleanField(default=True)),
                ('daily', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('avatar_url', models.CharField(unique=True, blank=True, null=True, max_length=200, verbose_name='Avatar Url')),
                ('github_id', models.IntegerField(unique=True, verbose_name='ID GitHub')),
                ('github_login', models.CharField(unique=True, max_length=100, verbose_name='Login GitHub')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('github_id', models.IntegerField(unique=True, verbose_name='ID GitHub')),
                ('number', models.IntegerField(unique=True)),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(blank=True, null=True, max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
                ('html_url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('close_at', models.DateTimeField(blank=True, null=True)),
                ('update_at', models.DateTimeField()),
                ('due_on', models.DateTimeField(blank=True, null=True)),
                ('assignee', models.ForeignKey(to='journal.Developer', blank=True, null=True, related_name='assignee_issues')),
                ('closed_by', models.ForeignKey(to='journal.Developer', blank=True, null=True, related_name='closedby_issues')),
                ('creator', models.ForeignKey(to='journal.Developer', related_name='creator_issues')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.TextField()),
                ('color', models.CharField(blank=True, null=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('email', models.EmailField(unique=True, max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('github_id', models.IntegerField(unique=True, verbose_name='ID GitHub')),
                ('number', models.IntegerField(unique=True)),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(blank=True, null=True, max_length=200)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('github_id', models.IntegerField(unique=True, verbose_name='ID GitHub')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('html_url', models.CharField(blank=True, null=True, max_length=200)),
                ('avatar_url', models.TextField(blank=True, null=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('github_id', models.IntegerField(unique=True, verbose_name='ID GitHub')),
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
            field=models.ForeignKey(to='journal.Developer', blank=True, null=True, related_name='sender_miletones'),
        ),
        migrations.AddField(
            model_name='manager',
            name='organization',
            field=models.ManyToManyField(related_name='journal_manager', to='journal.Organization', db_column='user_organization'),
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
            field=models.ForeignKey(to='journal.Developer', blank=True, null=True, related_name='sender_issues'),
        ),
        migrations.AddField(
            model_name='developer',
            name='organization',
            field=models.ManyToManyField(related_name='journal_developer', to='journal.Organization', db_column='user_organization'),
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
