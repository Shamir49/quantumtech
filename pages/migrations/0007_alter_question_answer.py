# Generated by Django 4.2.2 on 2023-08-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_review_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
