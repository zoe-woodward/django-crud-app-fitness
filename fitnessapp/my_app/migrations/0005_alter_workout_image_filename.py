# Generated by Django 4.2.18 on 2025-02-20 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_workout_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='image_filename',
            field=models.URLField(default='https://example.com/images/logo.avif', max_length=255),
        ),
    ]
