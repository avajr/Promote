# Generated by Django 4.2.7 on 2024-05-02 19:09

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=255, verbose_name="title")),
                ("short_description", models.TextField()),
                ("content", ckeditor.fields.RichTextField()),
                ("cover_img", models.ImageField(upload_to="blogs/")),
            ],
            options={
                "verbose_name": "Blog",
                "verbose_name_plural": "Blogs",
            },
        ),
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=100, verbose_name="category")),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="CaseStudy",
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
                ("title", models.CharField(max_length=255, verbose_name="title")),
                ("short_description", models.TextField()),
                ("content", ckeditor.fields.RichTextField()),
                ("cover_img", models.ImageField(upload_to="case_studies/")),
                (
                    "company_logo",
                    models.ImageField(upload_to="case_studies/companies/"),
                ),
                ("client", models.CharField(max_length=100, verbose_name="client")),
                ("platform", models.CharField(max_length=100, verbose_name="platform")),
                ("results", models.PositiveBigIntegerField(verbose_name="results")),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="common.service",
                    ),
                ),
            ],
            options={
                "verbose_name": "Case Study",
                "verbose_name_plural": "Case Studies",
            },
        ),
    ]
