# Generated by Django 4.1.3 on 2022-12-13 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("movies", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="movieorder",
            name="buyer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="buys",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="movie",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="movies",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
