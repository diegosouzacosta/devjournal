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
                ('name', models.CharField(unique=True, max_length=150)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('avatar_url', models.CharField(null=True, unique=True, blank=True, verbose_name='Avatar Url', max_length=200)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('github_login', models.CharField(verbose_name='Login GitHub', unique=True, max_length=100)),
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
                ('title', models.CharField(null=True, blank=True, max_length=200)),
                ('body', models.TextField(null=True, blank=True)),
                ('html_url', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField()),
                ('close_at', models.DateTimeField(null=True, blank=True)),
                ('update_at', models.DateTimeField()),
                ('due_on', models.DateTimeField(null=True, blank=True)),
                ('assignee', models.ForeignKey(null=True, related_name='assignee_issues', blank=True, to='journal.Developer')),
                ('closed_by', models.ForeignKey(null=True, related_name='closedby_issues', blank=True, to='journal.Developer')),
                ('creator', models.ForeignKey(to='journal.Developer', related_name='creator_issues')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('color', models.CharField(null=True, blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('number', models.IntegerField(unique=True)),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(null=True, blank=True, max_length=200)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('html_url', models.CharField(null=True, blank=True, max_length=200)),
                ('avatar_url', models.TextField(null=True, blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('html_url', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField()),
                ('creator', models.ForeignKey(to='journal.Developer', related_name='projects')),
                ('organization', models.ForeignKey(to='journal.Organization', related_name='projects')),
            ],
        ),
        migrations.AddField(
            model_name='milestone',
            name='project',
            field=models.ForeignKey(related_name='milestones', db_column='project_id', to='journal.Project'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='sender',
            field=models.ForeignKey(null=True, related_name='sender_miletones', blank=True, to='journal.Developer'),
        ),
        migrations.AddField(
            model_name='manager',
            name='organization',
            field=models.ManyToManyField(db_column='user_organization', to='journal.Organization', related_name='journal_manager'),
        ),
        migrations.AddField(
            model_name='issue',
            name='label',
            field=models.ForeignKey(related_name='issues', db_column='label_id', to='journal.Label'),
        ),
        migrations.AddField(
            model_name='issue',
            name='milestone',
            field=models.ForeignKey(related_name='issues', db_column='milestone_id', to='journal.Milestone'),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(related_name='issues', db_column='project_id', to='journal.Project'),
        ),
        migrations.AddField(
            model_name='issue',
            name='sender',
            field=models.ForeignKey(null=True, related_name='sender_issues', blank=True, to='journal.Developer'),
        ),
        migrations.AddField(
            model_name='developer',
            name='organization',
            field=models.ManyToManyField(db_column='user_organization', to='journal.Organization', related_name='journal_developer'),
        ),
        migrations.AddField(
            model_name='config',
            name='manager',
            field=models.ForeignKey(to='journal.Manager'),
        ),
        migrations.AddField(
            model_name='config',
            name='projects',
            field=models.ManyToManyField(db_column='config_manager', to='journal.Project', related_name='configs'),
        ),
    ]
