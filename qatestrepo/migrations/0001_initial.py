# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QATestPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('testplanName', models.CharField(max_length=1000)),
                ('owner', models.CharField(max_length=200)),
                ('release', models.CharField(max_length=100)),
                ('team', models.CharField(max_length=100)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('modifiedTime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
