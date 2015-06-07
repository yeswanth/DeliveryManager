# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryboyorder',
            name='status',
            field=models.CharField(default=b'INCOMPLETE', max_length=20, choices=[(b'INCOMPLETE', b'INCOMPLETE'), (b'COMPLETED', b'COMPLETED')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='fb_key',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
