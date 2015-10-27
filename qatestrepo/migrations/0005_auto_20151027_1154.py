# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qatestrepo', '0004_auto_20151027_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qatestplan',
            old_name='testPlan_name',
            new_name='testplan_name',
        ),
    ]
