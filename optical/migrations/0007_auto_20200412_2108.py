# Generated by Django 3.0.5 on 2020-04-13 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optical', '0006_auto_20200412_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='owner',
            new_name='user',
        ),
    ]
