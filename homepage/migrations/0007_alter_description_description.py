# Generated by Django 4.1.13 on 2024-03-18 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_alter_description_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
