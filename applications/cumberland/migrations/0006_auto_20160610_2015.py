# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cumberland', '0005_auto_20160610_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipient',
            old_name='receivers',
            new_name='receiver',
        ),
        migrations.AlterField(
            model_name='box',
            name='expiring_date',
            field=models.DateField(help_text='Select a date of Expiration. By default it is set two 1 months', default=datetime.datetime(2016, 7, 11, 0, 15, 39, 682745, tzinfo=utc), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='box',
            name='title',
            field=models.CharField(verbose_name='Title', help_text='Add a title on you Suggestion Box i.e: How did you find my presentation', max_length=60),
        ),
    ]
