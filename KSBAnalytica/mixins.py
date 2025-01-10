from cloudinary.models import CloudinaryField
from django.db import models


class BaseModel(models.Model):
    image = CloudinaryField(
        'image',
        default='https://res.cloudinary.com/ddvtmmwk5/image/upload/v1234567890/placeholder.png',
    )
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    class Meta:
        abstract = True


class LanguageMixin(models.Model):
    language = models.ForeignKey(
        'common.AppLanguage',  # Correct the reference to the `Applanguage` model
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="%(class)s_language",
        help_text="The language this entry applies to.",
    )

    class Meta:
        abstract = True
