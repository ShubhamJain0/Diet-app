# Generated by Django 2.2.2 on 2019-12-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diet', '0016_auto_20191205_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietdata',
            name='query',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
