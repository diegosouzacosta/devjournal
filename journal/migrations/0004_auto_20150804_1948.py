# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_remove_milestone_sender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='config',
            options={'verbose_name': 'Configuration'},
        ),
        migrations.AlterField(
            model_name='issue',
            name='label',
            field=models.ForeignKey(to='journal.Label', related_name='issues', blank=True, null=True),
        ),
    ]
