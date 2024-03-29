# Generated by Django 5.0.2 on 2024-02-26 22:01

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0009_alter_vehicle_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='car_features',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('CC', 'Cruise Control'), ('AI', 'Audio Interface'), ('A', 'Airbags'), ('AC', 'Air Conditioning'), ('SH', 'Seat Heating'), ('PA', 'ParkAssist'), ('PS', 'Power Steering'), ('RC', 'Reversing Camera'), ('AS', 'Auto Start/Stop')], default='A', max_length=2),
        ),
    ]
