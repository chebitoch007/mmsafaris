# ============================================
# core/urls.py
# ============================================
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tours/', views.tours, name='tours'),
    path('tours/<slug:slug>/', views.tour_detail, name='tour_detail'),
    path('tours/<slug:slug>/book/', views.booking, name='booking'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
