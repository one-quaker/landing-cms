# Generated by Django 2.2 on 2019-04-18 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='content',
            new_name='text',
        ),
    ]
