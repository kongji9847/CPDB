# Generated by Django 3.2.11 on 2022-03-26 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_property_cpfigure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='CpFigure',
        ),
    ]
