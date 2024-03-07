# Generated by Django 5.0.2 on 2024-03-07 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0013_alter_vehicle_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordervehicle',
            name='order_status',
            field=models.IntegerField(choices=[(0, 'Cancelled'), (1, 'Placed'), (2, 'Shipped'), (3, 'Delivered')], default=1),
        ),
    ]