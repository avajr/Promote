from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


# Job model (to define the role of staff in the company)
class JobModel(models.Model):
    job = models.CharField("job", max_length=128)

    def __str__(self):
        return self.job

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"


# Staff model (Auth model for staff on company)
class StaffModel(AbstractUser):
    picture = models.ImageField(upload_to="staff/")
    username = models.CharField("username", max_length=150, null=True, blank=True, unique=True, error_messages={
        "unique": "A user with that username already exists.",
    }, )
    first_name = models.CharField("first name", max_length=150)
    last_name = models.CharField("last name", max_length=150)
    email = models.EmailField("email address")
    password = models.CharField("password", max_length=128)
    is_staff = models.BooleanField(
        "staff status",
        default=True,
        help_text="Designates whether the user can log into this admin site.",
    ),
    job = models.ForeignKey(JobModel, on_delete=models.PROTECT)
    instagram_url = models.CharField("instagram url", max_length=300, blank=True, null=True)
    facebook_url = models.CharField("facebook url", max_length=300, blank=True, null=True)
    twitter_url = models.CharField("twitter url", max_length=300, blank=True, null=True)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"


# FAQ model (for Frequently Asked Questions)
class FAQModel(models.Model):
    question = models.CharField("question", max_length=255)
    answer = models.CharField("answer", max_length=255)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"


# Service model
class ServiceModel(models.Model):
    icon = models.ImageField(upload_to="service-icons/")
    name = models.CharField("service", max_length=100)
    description = models.TextField("description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


# Contact model (for all contacted information)
class ContactModel(models.Model):
    full_name  = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField("email address")
    subject = models.CharField("subject", max_length=100)
    message = models.TextField("message")
    created_at = models.DateField("created date", auto_now_add=True)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


# Testimonial model (for company's feedbacks)
class TestimonialModel(models.Model):
    company = models.ImageField(upload_to="clients/company/")
    # company = models.CharField(max_length=100)
    feedback = models.TextField("feedback")
    client_picture = models.ImageField(upload_to="clients/picture/")
    client_full_name = models.CharField(max_length=100)
    client_job = models.ForeignKey(JobModel, on_delete=models.RESTRICT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.client_full_name

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


# Case Study model
class CaseStudyModel(models.Model):
    cover_img = models.ImageField(upload_to="case_studies/")
    company_logo = models.ImageField(upload_to="case_studies/companies/")
    title = models.CharField("title", max_length=255)
    client = models.CharField("client", max_length=100)
    service = models.ForeignKey(ServiceModel, on_delete=models.RESTRICT)
    platform = models.CharField("platform", max_length=100)
    results = models.PositiveBigIntegerField("results")
    short_description = models.TextField()
    content = RichTextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Case Study"
        verbose_name_plural = "Case Studies"


# Category model (for category of blogs)
class CategoryModel(models.Model):
    name = models.CharField("category", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


# Blog model
class BlogModel(models.Model):
    title = models.CharField("title", max_length=255)
    short_description = models.TextField()
    content = RichTextField()
    cover_img = models.ImageField(upload_to="blogs/")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
