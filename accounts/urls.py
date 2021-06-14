from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('activate/', views.activate, name="activate"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
