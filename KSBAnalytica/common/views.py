from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from KSBAnalytica import settings
from KSBAnalytica.common.forms import ContactForm
from KSBAnalytica.common.models import AboutCompetence, FrequentQuestion, AppLanguage


# Create your views here.
def home_view(request):
    return render(request, 'common/base.html')


class AboutCompetenceListView(ListView):
    model = AboutCompetence
    template_name = 'common/about_us.html'
    context_object_name = 'competences'
    paginate_by = 10

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
            return AboutCompetence.objects.none()

        # Filter AboutCompetence by the fetched AppLanguage
        return AboutCompetence.objects.filter(language=active_language)


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"New Contact Form Submission from {name}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            try:
                send_mail(
                    subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )

            except Exception as e:
                print("Error sending email:", e)

            return redirect('contact-success')

    else:
        form = ContactForm(user=request.user)

    return render(request, 'common/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'common/contact_success.html')


def faq_view_english(request):
    """
    View to display the FAQ page.
    """
    faqs = FrequentQuestion.objects.filter(language__language="English")
    return render(request, 'common/faq.html', {'faqs': faqs})
