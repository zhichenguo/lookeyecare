# Generated by Django 3.0.5 on 2020-05-05 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0013_remove_address_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=22),
        ),
    ]
