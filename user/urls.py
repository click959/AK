from django.contrib import admin
from django.urls import path , include
from user import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/' , views.login),
    path('/', views.userlogin),
]
