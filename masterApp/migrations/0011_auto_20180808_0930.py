# Generated by Django 2.1 on 2018-08-08 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masterApp', '0010_auto_20180808_0923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shift',
            old_name='from_time',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='shift',
            old_name='to_time',
            new_name='start_time',
        ),
    ]