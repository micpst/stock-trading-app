# Generated by Django 4.0.6 on 2022-09-01 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='ticker',
            new_name='symbol',
        ),
    ]
