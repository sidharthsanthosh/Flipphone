# Generated by Django 5.0 on 2024-01-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=20)),
                ('eml', models.EmailField(max_length=254)),
                ('pas', models.CharField(max_length=20)),
            ],
        ),
    ]
