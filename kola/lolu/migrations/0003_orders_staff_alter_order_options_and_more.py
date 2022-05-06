# Generated by Django 4.0.2 on 2022-03-13 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lolu', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('stationary', 'stationary'), ('electronics', 'electronics'), ('food', 'foods')], max_length=20, null=True)),
                ('quantity', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'product'},
        ),
    ]
