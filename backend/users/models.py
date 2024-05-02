from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for My Awesome Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


# Job model (to define the role of staff in the company)
class Job(models.Model):
    title = models.CharField("title", max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"


# Staff model (Auth model for staff on company)
class Staff(models.Model):
    picture = models.ImageField(upload_to="staff/")

    username = models.CharField("username", max_length=150, null=True, blank=True, unique=True, error_messages={
        "unique": "A user with that username already exists.",
    }, )

    first_name = models.CharField("first name", max_length=150)
    last_name = models.CharField("last name", max_length=150)
    email = models.EmailField("email address")

    job = models.ForeignKey(Job, on_delete=models.PROTECT)

    instagram_url = models.CharField("instagram url", max_length=300, blank=True, null=True)
    facebook_url = models.CharField("facebook url", max_length=300, blank=True, null=True)
    twitter_url = models.CharField("twitter url", max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"
