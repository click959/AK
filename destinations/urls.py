from django.contrib import admin
from django.urls import path , re_path
from destinations import views

urlpatterns = [
    path('', views.destinations , name = 'destinations'),
    path('<int:id>' , views.destination , name = 'destination')
]