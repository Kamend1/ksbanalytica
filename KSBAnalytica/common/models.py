from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from KSBAnalytica.mixins import BaseModel

UserModel = get_user_model()


# Create your models here.
class AboutCompetence(BaseModel, models.Model):
    language = models.ForeignKey(
        'common.AppLanguage',  # Correct the reference to the `Applanguage` model
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="%(class)s_language",
        help_text="The language this entry applies to.",
    )


class Profile(models.Model):
    profile_image = models.URLField(null=True, blank=True)
    profile_link = models.URLField(null=True, blank=True)
    profile_caption = models.CharField(max_length=150)
    team_member = models.BooleanField(default=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    user = models.OneToOneField(to=UserModel, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,20}$',
                message="Phone number must be in E.164 format, e.g., +359123456789",
            )
        ],
        help_text="Enter phone number in E.164 format, e.g., +359123456789",
    )


class FrequentQuestion(models.Model):
    title = models.TextField(null=False, blank=False)
    answer = models.TextField(null=False, blank=False)
    language = models.ForeignKey(
        'common.AppLanguage',  # Correct the reference to the `Applanguage` model
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="%(class)s_language",
        help_text="The language this entry applies to.",
    )


class AppLanguage(models.Model):
    language = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.language}"
