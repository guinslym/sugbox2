# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import basis.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('updated_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('identify', models.BooleanField(default=False)),
                ('activate', models.BooleanField(default=False)),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('activation_key', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('expiring_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Recipients',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('updated_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('receivers', models.EmailField(blank=True, max_length=254, null=True)),
                ('box', models.ForeignKey(related_name='recipients', to='cumberland.Box')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('updated_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('comment', models.CharField(blank=True, verbose_name='', max_length=250, null=True)),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('box', models.ForeignKey(related_name='suggies', to='cumberland.Box')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
