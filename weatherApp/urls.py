from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name="home"),
    path('API/', views.api_pokemon, name="API"),
]
