# Generated by Django 5.0.6 on 2024-05-16 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cakes', '0002_masters_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reklama', models.URLField(null=True)),
                ('image', models.ImageField(upload_to='product/products')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('locations', models.ManyToManyField(to='cakes.locations')),
                ('sweets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakes.sweets')),
            ],
        ),
    ]