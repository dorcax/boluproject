# Generated by Django 4.0.2 on 2022-03-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lolu', '0003_orders_staff_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('delivered', 'delivered'), ('out for delivery', 'out for delivery')], max_length=200, null=True),
        ),
    ]
