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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('weekly', models.BooleanField(default=True)),
                ('daily', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('avatar_url', models.CharField(max_length=200, verbose_name='Avatar Url', unique=True, null=True, blank=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub')),
                ('number', models.IntegerField()),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=200, blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('html_url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('close_at', models.DateTimeField(blank=True, null=True)),
                ('update_at', models.DateTimeField()),
                ('due_on', models.DateTimeField(blank=True, null=True)),
                ('assignee', models.ForeignKey(null=True, to='journal.Developer', blank=True, related_name='assignee_issues')),
                ('closed_by', models.ForeignKey(null=True, to='journal.Developer', blank=True, related_name='closedby_issues')),
                ('creator', models.ForeignKey(related_name='creator_issues', to='journal.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField()),
                ('color', models.CharField(max_length=10, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub')),
                ('number', models.IntegerField()),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=200, blank=True, null=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('html_url', models.CharField(max_length=200, blank=True, null=True)),
                ('avatar_url', models.TextField(max_length=200, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
            field=models.ForeignKey(db_column='project_id', to='journal.Project', related_name='milestones'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='sender',
            field=models.ForeignKey(null=True, to='journal.Developer', blank=True, related_name='sender_miletones'),
        ),
        migrations.AddField(
            model_name='manager',
            name='organization',
            field=models.ManyToManyField(db_column='user_organization', to='journal.Organization', related_name='journal_manager'),
        ),
        migrations.AddField(
            model_name='issue',
            name='label',
            field=models.ForeignKey(db_column='label_id', to='journal.Label', related_name='issues'),
        ),
        migrations.AddField(
            model_name='issue',
            name='milestone',
            field=models.ForeignKey(db_column='milestone_id', to='journal.Milestone', related_name='issues'),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(db_column='project_id', to='journal.Project', related_name='issues'),
        ),
        migrations.AddField(
            model_name='issue',
            name='sender',
            field=models.ForeignKey(null=True, to='journal.Developer', blank=True, related_name='sender_issues'),
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
