# Generated by Django 5.1.1 on 2024-11-03 07:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_order_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitem',
            name='expiry_days',
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
