# Generated by Django 2.2.2 on 2019-12-04 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dietdata',
            old_name='Age',
            new_name='Age_now',
        ),
    ]
