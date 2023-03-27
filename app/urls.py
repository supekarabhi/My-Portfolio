from django.contrib import admin
from django.urls import path,include
from app import views
from .views import HomeTemplateView

urlpatterns = [
  
    path('',HomeTemplateView.as_view(),name="index"),
    
]
