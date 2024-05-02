# Generated by Django 4.2.7 on 2024-05-02 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0002_job_staff"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("full_name", models.CharField(max_length=100)),
                ("company", models.CharField(max_length=100)),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="email address"),
                ),
                ("subject", models.CharField(max_length=100, verbose_name="subject")),
                ("message", models.TextField(verbose_name="message")),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contacts",
            },
        ),
        migrations.CreateModel(
            name="FAQ",
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
                ("question", models.CharField(max_length=255, verbose_name="question")),
                ("answer", models.CharField(max_length=255, verbose_name="answer")),
            ],
            options={
                "verbose_name": "FAQ",
                "verbose_name_plural": "FAQs",
            },
        ),
        migrations.CreateModel(
            name="Service",
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
                ("icon", models.ImageField(upload_to="service-icons/")),
                ("title", models.CharField(max_length=100, verbose_name="service")),
                ("description", models.TextField(verbose_name="description")),
            ],
            options={
                "verbose_name": "Service",
                "verbose_name_plural": "Services",
            },
        ),
        migrations.CreateModel(
            name="Testimonial",
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
                ("company", models.ImageField(upload_to="clients/company/")),
                ("feedback", models.TextField(verbose_name="feedback")),
                ("client_picture", models.ImageField(upload_to="clients/picture/")),
                ("client_full_name", models.CharField(max_length=100)),
                (
                    "client_job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="users.job"
                    ),
                ),
            ],
            options={
                "verbose_name": "Testimonial",
                "verbose_name_plural": "Testimonials",
            },
        ),
    ]
