# Generated by Django 5.0.3 on 2024-05-25 06:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_job_person_alter_genre_name_movie_moviereview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereview',
            name='rating',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]