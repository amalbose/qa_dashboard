# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qatestrepo', '0003_auto_20151027_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qatestplan',
            old_name='testplan_name',
            new_name='testPlan_name',
        ),
        migrations.AlterField(
            model_name='qatestplan',
            name='release',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='qatestplan',
            name='team',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
