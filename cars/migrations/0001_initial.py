# Generated by Django 5.1.3 on 2024-12-04 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
