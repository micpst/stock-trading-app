# Generated by Django 4.0.6 on 2022-08-30 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('STANDARD', 'Standard'), ('PROFESSIONAL', 'Professional'), ('DEMO', 'Demo')], max_length=12)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('CLOSED', 'Closed'), ('SUSPENDED', 'Suspended')], default='ACTIVE', max_length=9)),
                ('balance', models.DecimalField(decimal_places=4, max_digits=19)),
                ('currency', models.CharField(choices=[('USD', 'American Dollar'), ('EUR', 'Euro'), ('PLN', 'Polish Zloty')], max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_account',
            },
        ),
    ]
