from django.shortcuts import render
from django.views.generic import ListView

from KSBAnalytica.common.models import AppLanguage
from KSBAnalytica.services.models import Service


# Create your views here.
class ServicesEnglishListView(ListView):
    model = Service
    template_name = "services/services-list-en.html"  # Path to the above template
    context_object_name = "services"  # Context variable for the template
    paginate_by = 12  # Optional: Number of items per page

    def get_queryset(self):
        # Map LANGUAGE_CODE to AppLanguage's language field
        print(f"Current language: {self.request.LANGUAGE_CODE}")
        language_code_map = {
            'en': 'English',
            'bg': 'Bulgarian',
        }
        active_language_name = language_code_map.get(self.request.LANGUAGE_CODE, 'English')

        # Fetch the AppLanguage instance
        active_language = AppLanguage.objects.filter(language=active_language_name).first()

        # If no match, return an empty queryset
        if not active_language:
            return Service.objects.none()

        # Filter AboutCompetence by the fetched AppLanguage
        return Service.objects.filter(language=active_language)
