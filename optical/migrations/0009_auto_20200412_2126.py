# Generated by Django 3.0.5 on 2020-04-13 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optical', '0008_auto_20200412_2113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Cart', 'verbose_name_plural': 'Carts'},
        ),
        migrations.RemoveField(
            model_name='cart',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='number',
        ),
    ]
