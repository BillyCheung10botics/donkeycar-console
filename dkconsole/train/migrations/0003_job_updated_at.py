# Generated by Django 3.0.4 on 2020-07-16 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0002_job_model_movie_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]