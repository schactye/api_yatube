# Generated by Django 2.2.16 on 2022-03-06 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220305_1441'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='comment',
            name='unique_comment',
        ),
    ]
