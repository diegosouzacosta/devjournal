# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('github_id', models.IntegerField(verbose_name='ID GitHub', unique=True)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('html_url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
