# Generated by Django 4.1.2 on 2023-01-15 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_producttype_remove_purchase_product_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="producttopurchase",
            name="finalPrice",
            field=models.PositiveIntegerField(),
        ),
    ]
