# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='email',
        ),
    ]
