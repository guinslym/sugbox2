# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cumberland', '0002_auto_20160609_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='description',
            field=models.CharField(max_length=250, null=True, blank=True, help_text='Your beautiful description of this Suggestion Box'),
        ),
        migrations.AlterField(
            model_name='box',
            name='email',
            field=models.EmailField(max_length=254, help_text='We will send you an email so that you can activate your new Suggestion Box'),
        ),
        migrations.AlterField(
            model_name='box',
            name='title',
            field=models.CharField(max_length=60, help_text='Add a title on you Suggestion Box i.e: How did you find my presentation'),
        ),
    ]
