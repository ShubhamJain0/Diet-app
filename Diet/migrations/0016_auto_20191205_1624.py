# Generated by Django 2.2.2 on 2019-12-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diet', '0015_auto_20191205_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietdata',
            name='query',
            field=models.IntegerField(null=True),
        ),
    ]
