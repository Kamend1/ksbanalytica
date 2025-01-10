from django.contrib import admin
from .models import Service, ServicePackage
from ..common.admin import BaseAdmin


# Register your models here.
@admin.register(Service)
class ServiceAdmin(BaseAdmin):
    """Admin configuration for the Service model."""
    pass


@admin.register(ServicePackage)
class ServicePackageAdmin(BaseAdmin):
    """Admin configuration for the ServicePackage model."""
    pass
