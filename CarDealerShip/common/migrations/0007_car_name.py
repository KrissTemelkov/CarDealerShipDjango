# Generated by Django 4.1.4 on 2022-12-17 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_remove_car_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]