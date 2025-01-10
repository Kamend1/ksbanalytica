from django.urls import path
from KSBAnalytica.services import views

urlpatterns = [
    path('services-en/', views.ServicesEnglishListView.as_view(), name='services-en')
]