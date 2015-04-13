# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150412_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
