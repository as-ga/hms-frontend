from django.contrib import admin
from django.urls import path, include
from accounts import views
urlpatterns = [
    path('login', views.loginuser, name="login"),
    path('register', views.SignupUser, name="register"),
    path('logout', views.logoutuser, name="logout"),

]
