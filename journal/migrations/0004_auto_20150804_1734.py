# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_remove_milestone_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='organization',
            field=models.ForeignKey(null=True, related_name='projects', to='journal.Organization', blank=True),
        ),
    ]
