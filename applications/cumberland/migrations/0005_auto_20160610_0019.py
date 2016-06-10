# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cumberland', '0004_auto_20160610_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='expiring_date',
            field=models.DateField(null=True, help_text='Select a date of Expiration. By default it is set two 1 months', default=datetime.datetime(2016, 7, 10, 4, 19, 21, 20730, tzinfo=utc), blank=True),
        ),
    ]
