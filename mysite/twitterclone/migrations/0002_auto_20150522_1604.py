# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
