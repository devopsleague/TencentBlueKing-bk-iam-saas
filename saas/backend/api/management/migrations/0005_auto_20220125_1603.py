# Generated by Django 2.2.24 on 2022-01-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20211130_1137'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='managementapiallowlistconfig',
            index_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='managementapiallowlistconfig',
            unique_together={('system_id', 'api')},
        ),

    ]
