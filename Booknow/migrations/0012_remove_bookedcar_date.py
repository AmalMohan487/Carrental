# Generated by Django 4.1.7 on 2023-03-11 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booknow', '0011_bookedcar_cancel_bookedcar_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookedcar',
            name='date',
        ),
    ]
