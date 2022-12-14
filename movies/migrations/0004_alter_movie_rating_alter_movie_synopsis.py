# Generated by Django 4.1.3 on 2022-12-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_rename_buyed_movie_movieorder_movie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="rating",
            field=models.CharField(
                choices=[
                    ("G", "General Audience"),
                    ("PG", "Parental Guidance Suggested"),
                    ("PG-13", "Parents Strongly"),
                    ("R", "Restricted"),
                    ("NC_17", "Adults Only"),
                    ("None", "Default"),
                ],
                default="None",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="synopsis",
            field=models.TextField(default=None, null=True),
        ),
    ]