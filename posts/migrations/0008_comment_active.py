# Generated by Django 3.2.4 on 2021-10-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_comment_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]