from django.urls import path
from . import views

urlpatterns = [
    path('graficos', views.graficos, name="graficos")


]