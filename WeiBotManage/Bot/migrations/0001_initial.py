# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('username', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=50, default='')),
                ('isValid', models.BooleanField(default=False)),
                ('cookies', models.CharField(max_length=500)),
                ('message_num', models.IntegerField(default=0)),
            ],
        ),
    ]
