# Generated by Django 5.0.6 on 2024-05-18 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0005_clients_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='discounts',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
