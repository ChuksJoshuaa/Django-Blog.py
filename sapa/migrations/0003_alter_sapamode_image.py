# Generated by Django 3.2.4 on 2021-09-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sapa', '0002_alter_sapamode_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sapamode',
            name='image',
            field=models.ImageField(height_field=100, upload_to='', width_field=200),
        ),
    ]
