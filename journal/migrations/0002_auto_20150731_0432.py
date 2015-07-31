# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='close_at',
            new_name='closed_at',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='milestone',
            old_name='close_at',
            new_name='closed_at',
        ),
        migrations.RenameField(
            model_name='milestone',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
