# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qatestrepo', '0002_auto_20151027_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qatestplan',
            old_name='testplanName',
            new_name='testplan_name',
        ),
    ]
