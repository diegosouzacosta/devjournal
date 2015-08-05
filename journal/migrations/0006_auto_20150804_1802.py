# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_auto_20150804_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='label',
            field=models.ForeignKey(blank=True, related_name='issues', to='journal.Label', null=True),
        ),
    ]
