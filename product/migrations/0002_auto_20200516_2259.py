# Generated by Django 3.0.5 on 2020-05-17 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Men'), ('W', 'Women'), ('K', 'Kid'), ('U', 'Unisex'), ('O', 'Other')], default='U', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('P', 'primary'), ('S', 'On Sale'), ('N', 'New')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='off_percentage',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='shape',
            field=models.CharField(blank=True, choices=[('RT', 'Rectangle'), ('RD', 'Round'), ('A', 'Aviator'), ('G', 'Geometric'), ('NA', 'NA')], default='NA', max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('SM', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('NA', 'NA')], default='NA', max_length=2),
        ),
    ]
