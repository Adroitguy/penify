# Generated by Django 2.2.2 on 2019-06-05 02:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0016_auto_20190605_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 5, 2, 56, 5, 457139, tzinfo=utc), editable=False, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='uid',
            field=models.CharField(default='4f9b1dba-7161-4516-9856-a512fcad2e4b', editable=False, max_length=50),
        ),
    ]
