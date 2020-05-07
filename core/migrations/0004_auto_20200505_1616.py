# Generated by Django 3.0.5 on 2020-05-05 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0012_remove_payment_cart'),
        ('core', '0003_auto_20200505_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='default_address',
        ),
        migrations.AddField(
            model_name='profile',
            name='default_billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_billing_address', to='shopping.Address'),
        ),
        migrations.AddField(
            model_name='profile',
            name='default_shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_shipping_address', to='shopping.Address'),
        ),
    ]
