# Generated by Django 4.2.4 on 2023-08-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_orderinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.BooleanField(default=False),
        ),
    ]
