# Generated by Django 4.1.4 on 2022-12-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
