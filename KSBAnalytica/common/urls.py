from django.urls import path
from KSBAnalytica.common import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about-us/', views.AboutCompetenceListView.as_view(), name='about-us'),
    path('contact-us-en/', views.contact, name='contact-us-en'),
    path('contact-success-en/', views.contact_success, name='contact-success'),
    path('faq-en/', views.faq_view_english, name='faq-en'),

]