# Generated by Django 5.0 on 2024-02-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipphoneapp', '0009_brand_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_tbl',
            name='brand',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
