from django.db import models

from utils.models import BaseModel
from users.models import Job


# FAQ model (for Frequently Asked Questions)
class FAQ(BaseModel):
    question = models.CharField("question", max_length=255)
    answer = models.CharField("answer", max_length=255)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"


# Service model
class Service(BaseModel):
    icon = models.ImageField(upload_to="service-icons/")
    title = models.CharField("service", max_length=100)
    description = models.TextField("description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


# Contact model (for all contacted information)
class Contact(BaseModel):
    full_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField("email address")
    subject = models.CharField("subject", max_length=100)
    message = models.TextField("message")

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


# Testimonial model (for company's feedbacks)

class Testimonial(BaseModel):
    company = models.ImageField(upload_to="clients/company/")
    feedback = models.TextField("feedback")

    client_picture = models.ImageField(upload_to="clients/picture/")
    client_full_name = models.CharField(max_length=100)
    client_job = models.ForeignKey(Job, on_delete=models.RESTRICT)

    def __str__(self):
        return self.client_full_name

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
