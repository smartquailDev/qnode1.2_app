# Generated by Django 3.2.15 on 2022-10-12 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20221006_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='departure_date_time',
            field=models.DateTimeField(null=True, verbose_name='Date & time for Departure to CC-floreana'),
        ),
    ]
