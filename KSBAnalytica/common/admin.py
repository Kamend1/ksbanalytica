from django.contrib import admin
from .models import AboutCompetence, Profile, FrequentQuestion, AppLanguage

from django.contrib import admin


# Register your models here.
# Base admin class for common configurations
class BaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'language')
    search_fields = ('title', 'description')
    list_filter = ('title',)


@admin.register(AboutCompetence)
class AboutCompetenceAdmin(BaseAdmin):
    """Admin configuration for the AboutCompetence model."""
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin configuration for the Profile model."""
    list_display = (
        'user',
        'team_member',
        'age',
        'phone_number',
        'profile_image',
        'profile_caption',
    )
    search_fields = ('user__username', 'profile_caption', 'phone_number')
    list_filter = ('team_member', 'age')
    readonly_fields = ('user',)


@admin.register(FrequentQuestion)
class FrequentQuestionAdmin(admin.ModelAdmin):
    """Admin configuration for the FrequentQuestion model."""
    list_display = ('title', 'answer', 'language')
    search_fields = ('title', 'answer')


@admin.register(AppLanguage)
class AppLanguageAdmin(admin.ModelAdmin):
    list_display = ('language',)