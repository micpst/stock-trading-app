# Generated by Django 4.0.6 on 2022-08-26 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceTicker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=4, max_digits=19)),
                ('time_epoch', models.DateTimeField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock')),
            ],
            options={
                'db_table': 'tbl_price_ticker',
            },
        ),
    ]
