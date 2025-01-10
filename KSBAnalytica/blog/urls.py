from django.urls import path
from KSBAnalytica.blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('tag/<slug:slug>/', views.tag_posts, name='tag_posts'),
]