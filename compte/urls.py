from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.accueil),
    path('dash/', views.dashboard, name='dash'),
    path('Cantine/', views.cantine, name='Cantine'),
    path('Assurance/', views.assurance, name='Assurance'),
]