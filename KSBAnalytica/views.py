from django.conf.urls.i18n import set_language as original_set_language
from django.utils.translation import activate, get_language
from django.http import HttpResponse, HttpResponseRedirect


def set_language(request):
    # Log the incoming language
    lang = request.POST.get('lang', 'Not provided')
    print(f"[DEBUG] Language switch requested: {lang}")

    # Call the original set_language view
    response = original_set_language(request)

    # Confirm if the language cookie was set
    if 'django_language' in response.cookies:
        print(f"[DEBUG] django_language cookie set to: {response.cookies['django_language'].value}")
    else:
        print("[DEBUG] django_language cookie not set.")

    return response


def set_language_debug(request):
    lang_code = request.POST.get('lang')
    print("[DEBUG] Received set_language request")
    print(f"[DEBUG] Current request method: {request.method}")

    if lang_code:
        print(f"[DEBUG] Requested language switch to: {lang_code}")
        activate(lang_code)
        request.session['django_language'] = lang_code
        print(f"[DEBUG] Language activated. Current language: {get_language()}")
        print(f"[DEBUG] Session 'django_language': {request.session.get('django_language')}")
    else:
        print("[DEBUG] No language code provided in the request.")

    referer = request.META.get('HTTP_REFERER', '/')
    response = HttpResponseRedirect(referer)

    # Set the django_language cookie explicitly
    response.set_cookie(
        key='django_language',
        value=lang_code,
        max_age=31536000,  # One year
        secure=True,       # Only if using HTTPS
        samesite='Lax'
    )

    print(f"[DEBUG] Cookies in response: {response.cookies}")
    return response

