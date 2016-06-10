# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import basis.models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cumberland', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(editable=False, default=basis.models._now)),
                ('updated_at', models.DateTimeField(editable=False, default=basis.models._now)),
                ('receivers', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.RemoveField(
            model_name='recipients',
            name='box',
        ),
        migrations.AlterField(
            model_name='box',
            name='email',
            field=models.EmailField(default=datetime.datetime(2016, 6, 10, 3, 53, 37, 526628, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Recipients',
        ),
        migrations.AddField(
            model_name='recipient',
            name='box',
            field=models.ForeignKey(related_name='recipients', to='cumberland.Box'),
        ),
    ]
