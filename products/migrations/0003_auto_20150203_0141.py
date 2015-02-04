# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productimage_product_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product_image',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
    ]
