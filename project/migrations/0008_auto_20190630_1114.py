# Generated by Django 2.2.1 on 2019-06-30 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20190629_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='owner',
            new_name='owner_id',
        ),
    ]
