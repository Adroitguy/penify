# Generated by Django 2.2.2 on 2019-06-07 02:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0034_auto_20190607_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='7fa729cd-7425-4332-9732-12df8e0968ce', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 7, 2, 46, 6, 821962, tzinfo=utc), verbose_name='updated at'),
        ),
    ]
