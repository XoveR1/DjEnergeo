# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name=b'date published')),
                ('category', models.ForeignKey(to='categories.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
