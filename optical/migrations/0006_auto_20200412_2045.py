# Generated by Django 3.0.5 on 2020-04-13 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optical', '0005_auto_20200412_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['create_time'], 'verbose_name': 'Cart', 'verbose_name_plural': 'Carts'},
        ),
    ]
