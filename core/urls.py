from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cv/', views.cv, name="cv"),
    path('reading/', views.reading, name="reading"),
]