# Generated by Django 5.0 on 2024-01-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipphoneapp', '0004_product_tbl_product_spec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_tbl',
            name='product_name',
            field=models.CharField(max_length=80),
        ),
    ]
