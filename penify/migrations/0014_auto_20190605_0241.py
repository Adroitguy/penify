# Generated by Django 2.2.2 on 2019-06-05 02:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0013_auto_20190605_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='uid',
            field=models.CharField(default='e360025e-2d24-460e-a220-f969d3672e93', editable=False, max_length=50),
        ),
    ]
