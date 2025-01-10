from django.db import models

from KSBAnalytica.mixins import BaseModel, LanguageMixin


# Create your models here.
class Service(BaseModel, LanguageMixin, models.Model):
    pass


class ServicePackage(BaseModel, LanguageMixin, models.Model):
    pass
