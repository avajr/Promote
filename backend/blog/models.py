from django.db import models
from ckeditor.fields import RichTextField

from utils.models import BaseModel
from common.models import Service


# Case Study model
class CaseStudy(BaseModel):
    title = models.CharField("title", max_length=255)
    short_description = models.TextField()
    content = RichTextField()

    cover_img = models.ImageField(upload_to="case_studies/")
    company_logo = models.ImageField(upload_to="case_studies/companies/")

    client = models.CharField("client", max_length=100)
    service = models.ForeignKey(Service, on_delete=models.RESTRICT)
    platform = models.CharField("platform", max_length=100)

    results = models.PositiveBigIntegerField("results")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Case Study"
        verbose_name_plural = "Case Studies"


# Category model (for category of blogs)
class Category(BaseModel):
    title = models.CharField("category", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


# Blog model
class Blog(BaseModel):
    title = models.CharField("title", max_length=255)
    short_description = models.TextField()
    content = RichTextField()

    cover_img = models.ImageField(upload_to="blogs/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
