# Generated by Django 2.1 on 2018-08-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterApp', '0014_auto_20180808_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='user_type',
            field=models.CharField(max_length=20),
        ),
    ]
