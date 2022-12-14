# Generated by Django 4.0.6 on 2022-09-07 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapi', '0007_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='date',
            new_name='odate',
        ),
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.date(2022, 9, 12), null=True),
        ),
    ]
