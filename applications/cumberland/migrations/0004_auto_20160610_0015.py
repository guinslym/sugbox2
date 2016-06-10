# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cumberland', '0003_auto_20160610_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='expiring_date',
            field=models.DateField(blank=True, null=True, help_text='Select a date of Expiration. By default it is set two 1 months'),
        ),
    ]
