# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('enquiry_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('subject', models.CharField(max_length='125', verbose_name='Subject')),
                ('message', models.TextField(max_length=500, verbose_name='Message')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='enquiry Time')),
                ('resolved', models.BooleanField(default=False)),
                ('remarks', models.TextField(max_length=512)),
            ],
        ),
    ]
