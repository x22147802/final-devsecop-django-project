# Generated by Django 4.2 on 2023-04-16 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cart_products',
            name='cart_product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]