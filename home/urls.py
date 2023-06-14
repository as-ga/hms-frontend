
from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),

    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('doctors', views.doctors, name="doctors"),
    path('appointment', views.appointment, name="appointment"),
    path('faq', views.faq, name="faq"),
    path('testimonials', views.testimonials, name="testimonials"),
    path('contact', views.contact, name="contact"),
]
