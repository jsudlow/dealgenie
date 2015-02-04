# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20150203_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product_image',
            field=models.ImageField(upload_to=b'products/static'),
            preserve_default=True,
        ),
    ]
