# Generated by Django 2.2.1 on 2019-07-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, choices=[('1', 'Web Designer'), ('2', 'Web Developer'), ('3', 'WordPress'), ('4', 'WooCommerce'), ('5', 'PHP, .Net')], max_length=20, null=True),
        ),
    ]
