# Generated by Django 3.2.4 on 2021-10-12 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_comment_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='post',
        ),
    ]
