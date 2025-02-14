# Generated by Django 5.0 on 2024-01-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipphoneapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40)),
                ('product_image', models.FileField(upload_to='picture')),
                ('product_price', models.IntegerField()),
                ('product_des', models.TextField(null=True)),
            ],
        ),
    ]
