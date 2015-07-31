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
                ('avatar_url', models.CharField(verbose_name='Avatar Url', max_length=200, null=True, blank=True, unique=True)),
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
                ('github_id', models.IntegerField(verbose_name='ID GitHub')),
                ('number', models.IntegerField()),
                ('action', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('body', models.TextField(null=True, blank=True)),
                ('html_url', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField()),
                ('close_at', models.DateTimeField(null=True, blank=True)),
                ('update_at', models.DateTimeField()),
                ('due_on', models.DateTimeField(null=True, blank=True)),
                ('assignee', models.ForeignKey(related_name='assignee_issues', to='journal.Developer', null=True, blank=True)),
                ('closed_by', models.ForeignKey(related_name='closedby_issues', to='journal.Developer', null=True, blank=True)),
                ('creator', models.ForeignKey(to='journal.Developer', related_name='creator_issues')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField()),
                ('color', models.CharField(max_length=10, null=True, blank=True)),
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
                ('github_id', models.IntegerField(verbose_name='ID GitHub')),
                ('number', models.IntegerField()),
                ('state', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
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
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('html_url', models.CharField(max_length=200, null=True, blank=True)),
                ('avatar_url', models.TextField(max_length=200, null=True, blank=True)),
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
                ('organization', models.ForeignKey(to='journal.Organization', related_name='projects')),
            ],
        ),
        migrations.AddField(
            model_name='milestone',
            name='project',
            field=models.ForeignKey(to='journal.Project', related_name='milestones'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='sender',
            field=models.ForeignKey(related_name='sender_miletones', to='journal.Developer', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='manager',
            name='organization',
            field=models.ManyToManyField(db_column='user_organization', related_name='journal_manager', to='journal.Organization'),
        ),
        migrations.AddField(
            model_name='label',
            name='project',
            field=models.ForeignKey(to='journal.Project'),
        ),
        migrations.AddField(
            model_name='issue',
            name='label',
            field=models.ForeignKey(to='journal.Label', related_name='issues'),
        ),
        migrations.AddField(
            model_name='issue',
            name='milestone',
            field=models.ForeignKey(to='journal.Milestone', related_name='issues'),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(to='journal.Project', related_name='issues'),
        ),
        migrations.AddField(
            model_name='issue',
            name='sender',
            field=models.ForeignKey(related_name='sender_issues', to='journal.Developer', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='developer',
            name='organization',
            field=models.ManyToManyField(db_column='user_organization', related_name='journal_developer', to='journal.Organization'),
        ),
        migrations.AddField(
            model_name='config',
            name='manager',
            field=models.ForeignKey(to='journal.Manager'),
        ),
        migrations.AddField(
            model_name='config',
            name='projects',
            field=models.ManyToManyField(db_column='config_manager', related_name='configs', to='journal.Project'),
        ),
    ]
