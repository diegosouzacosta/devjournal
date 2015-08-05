# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_auto_20150804_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='milestone',
            field=models.ForeignKey(to='journal.Milestone', blank=True, null=True, related_name='issues'),
        ),
    ]
