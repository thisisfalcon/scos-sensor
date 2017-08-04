# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0003_auto_20170803_0247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acquisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField()),
                ('sigmf_metadata', jsonfield.fields.JSONField()),
                ('data', models.BinaryField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('schedule_entry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acquisitions', to='schedule.ScheduleEntry')),
            ],
            options={
                'db_table': 'acquisitions',
                'ordering': ('created',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='acquisition',
            unique_together=set([('schedule_entry', 'task_id')]),
        ),
    ]
