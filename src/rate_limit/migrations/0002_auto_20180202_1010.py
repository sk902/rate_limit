# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-02-02 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import djchoices.choices
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rate_limit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientRateLimitConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(db_index=True, max_length=255, unique=True)),
                ('specialization', models.CharField(blank=True, choices=[('GLOBAL', 'GLOBAL'), ('METHOD', 'METHOD'), ('API', 'API')], max_length=10, null=True, validators=[djchoices.choices.ChoicesValidator({'API': 'API', 'GLOBAL': 'GLOBAL', 'METHOD': 'METHOD'})])),
                ('end_point', models.TextField(null=True)),
                ('limit_sec', models.IntegerField(default=-1)),
                ('limit_min', models.IntegerField(default=-1)),
                ('limit_hour', models.IntegerField(default=-1)),
                ('limit_week', models.IntegerField(default=-1)),
                ('limit_month', models.IntegerField(default=-1)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
            ],
            options={
                'db_table': 'client_rate_limit_config',
            },
        ),
        migrations.DeleteModel(
            name='RateLimitConfig',
        ),
    ]
