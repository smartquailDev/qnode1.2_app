# Generated by Django 3.2.13 on 2022-08-12 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_translations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttranslation',
            name='available',
        ),
    ]