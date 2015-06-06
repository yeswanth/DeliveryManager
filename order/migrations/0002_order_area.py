# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='area',
            field=models.CharField(default='BTM', max_length=30, choices=[(b'BTM', b'BTM'), (b'KORAMANGALA', b'KORAMANGALA'), (b'INDIRA NAGAR', b'INDIRA NAGAR')]),
            preserve_default=False,
        ),
    ]
