from django.contrib import admin
from django.urls import path
from core import views
from posts import views

urlpatterns = [
    path('posts/', views.posts, name="posts"),
    path('posts/<slug:slug>/', views.post, name="post_detail"),
]