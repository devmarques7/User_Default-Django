# Generated by Django 4.1.3 on 2022-12-13 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(default=None, max_length=10, null=True)),
                ("rating", models.CharField(default="G", max_length=20)),
                (
                    "synopsis",
                    models.CharField(
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
            ],
        ),
        migrations.CreateModel(
            name="MovieOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("buyed_at", models.DateTimeField(auto_now_add=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "buyed_movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buys",
                        to="movies.movie",
                    ),
                ),
            ],
        ),
    ]
