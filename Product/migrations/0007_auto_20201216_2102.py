# Generated by Django 3.0.1 on 2020-12-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_cart_cart_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='cart_name',
            field=models.CharField(max_length=200),
        ),
    ]
