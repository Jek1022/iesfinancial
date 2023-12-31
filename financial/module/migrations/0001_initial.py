# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-31 09:15
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
        ('mainmodule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(max_length=250)),
                ('segment', models.CharField(max_length=50, unique=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 1, 31, 17, 15, 47, 572412))),
                ('isdeleted', models.IntegerField(default=0)),
                ('django_content_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='django_content_type_id', to='contenttypes.ContentType', validators=[django.core.validators.MinValueValidator(1)])),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='module_enter', to=settings.AUTH_USER_MODEL)),
                ('mainmodule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainmodule_id', to='mainmodule.Mainmodule', validators=[django.core.validators.MinValueValidator(1)])),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='module_modify', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'module',
                'permissions': (('view_module', 'Can view module'),),
            },
        ),
    ]
