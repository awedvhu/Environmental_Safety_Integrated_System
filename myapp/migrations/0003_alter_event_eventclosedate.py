# Generated by Django 3.2.10 on 2021-12-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20211230_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventCloseDate',
            field=models.DateTimeField(null=True),
        ),
    ]