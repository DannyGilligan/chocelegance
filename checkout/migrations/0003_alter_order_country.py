# Generated by Django 3.2.24 on 2024-03-03 06:16

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20240302_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]