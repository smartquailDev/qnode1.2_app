# Generated by Django 3.2.15 on 2022-10-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20221006_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='arrival_date_time',
            field=models.DateTimeField(null=True, verbose_name='Date & time for Arrival to CC-floreana'),
        ),
        migrations.AlterField(
            model_name='order',
            name='departure_date_time',
            field=models.DateTimeField(null=True, verbose_name='Date & time for Arrival to CC-floreana'),
        ),
    ]