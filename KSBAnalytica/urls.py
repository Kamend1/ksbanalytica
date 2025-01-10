from django.conf.urls.i18n import i18n_patterns, set_language
from django.contrib import admin
from django.urls import path, include



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('KSBAnalytica.common.urls')),  # Wrap your main app URLs
    path('services/', include('KSBAnalytica.services.urls')),
    path('blog/', include('KSBAnalytica.blog.urls')),
    path('accounts/', include('KSBAnalytica.accounts.urls')),
]

urlpatterns += [
    path('i18n/setlang/', set_language, name='set_language'),
]