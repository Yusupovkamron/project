# Generated by Django 5.0.6 on 2024-05-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='name',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='title',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
