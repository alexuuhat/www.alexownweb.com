from django.urls import path
from . import views

urlpatterns = [
    path('', views.home)
] #view of Default page or Home page
