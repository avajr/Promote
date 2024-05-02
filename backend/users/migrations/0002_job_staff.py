# Generated by Django 4.2.7 on 2024-05-02 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(max_length=128, verbose_name="title")),
            ],
            options={
                "verbose_name": "Job",
                "verbose_name_plural": "Jobs",
            },
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("picture", models.ImageField(upload_to="staff/")),
                (
                    "username",
                    models.CharField(
                        blank=True,
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        max_length=150,
                        null=True,
                        unique=True,
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=150, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=150, verbose_name="last name"),
                ),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="email address"),
                ),
                (
                    "instagram_url",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="instagram url",
                    ),
                ),
                (
                    "facebook_url",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="facebook url",
                    ),
                ),
                (
                    "twitter_url",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="twitter url",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="users.job"
                    ),
                ),
            ],
            options={
                "verbose_name": "Staff",
                "verbose_name_plural": "Staff",
            },
        ),
    ]
