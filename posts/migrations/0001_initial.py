# Generated by Django 4.1.7 on 2023-03-31 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=300)),
                ("content", models.TextField(blank=True)),
                (
                    "house",
                    models.CharField(
                        choices=[
                            ("Gryffindor", "Gryffindor"),
                            ("Slytherin", "Slytherin"),
                            ("Ravenclaw", "Ravenclaw"),
                            ("Hufflepuff", "Hufflepuff"),
                        ],
                        max_length=45,
                        null=True,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="../default_post_aypa8e",
                        upload_to="images/",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
