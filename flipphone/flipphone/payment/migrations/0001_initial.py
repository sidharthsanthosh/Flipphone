# Generated by Django 5.0 on 2024-02-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=25)),
                ('address', models.TextField(max_length=60)),
                ('mobile', models.IntegerField()),
                ('Pin', models.IntegerField()),
                ('products', models.TextField(max_length=250)),
                ('amount', models.IntegerField()),
                ('pay_method', models.CharField(max_length=25)),
                ('order_id', models.TextField(max_length=150)),
                ('o_date', models.CharField(max_length=25)),
                ('d_date', models.CharField(max_length=25)),
            ],
        ),
    ]
