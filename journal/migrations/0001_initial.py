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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('weekly', models.BooleanField(default=True)),
                ('daily', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('avatar_url', models.CharField(blank=True, verbose_name='Avatar Url', unique=True, max_length=200, null=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub')),
                ('number', models.IntegerField()),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('html_url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('close_at', models.DateTimeField(blank=True, null=True)),
                ('update_at', models.DateTimeField()),
                ('due_on', models.DateTimeField(blank=True, null=True)),
                ('assignee', models.ForeignKey(related_name='assignee_issues', null=True, blank=True, to='journal.Developer')),
                ('closed_by', models.ForeignKey(related_name='closedby_issues', null=True, blank=True, to='journal.Developer')),
                ('creator', models.ForeignKey(related_name='creator_issues', to='journal.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('color', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('number', models.IntegerField(unique=True)),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('html_url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('close_at', models.DateTimeField(blank=True, null=True)),
                ('update_at', models.DateTimeField()),
                ('due_on', models.DateTimeField(blank=True, null=True)),
                ('creator', models.ForeignKey(related_name='creator_milestones', to='journal.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('html_url', models.CharField(blank=True, max_length=200, null=True)),
                ('avatar_url', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('html_url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('creator', models.ForeignKey(related_name='projects', to='journal.Developer')),
                ('organization', models.ForeignKey(related_name='projects', to='journal.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='milestone',
            name='project',
            field=models.ForeignKey(related_name='milestones', to='journal.Project', db_column='project_id'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='sender',
            field=models.ForeignKey(related_name='sender_miletones', null=True, blank=True, to='journal.Developer'),
        ),
        migrations.AddField(
            model_name='manager',
            name='organization',
            field=models.ManyToManyField(related_name='journal_manager', to='journal.Organization', db_column='user_organization'),
        ),
        migrations.AddField(
            model_name='issue',
            name='label',
            field=models.ForeignKey(related_name='issues', to='journal.Label', db_column='label_id'),
        ),
        migrations.AddField(
            model_name='issue',
            name='milestone',
            field=models.ForeignKey(related_name='issues', to='journal.Milestone', db_column='milestone_id'),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(related_name='issues', to='journal.Project', db_column='project_id'),
        ),
        migrations.AddField(
            model_name='issue',
            name='sender',
            field=models.ForeignKey(related_name='sender_issues', null=True, blank=True, to='journal.Developer'),
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
            field=models.ManyToManyField(related_name='configs', to='journal.Project', db_column='config_manager'),
        ),
    ]
