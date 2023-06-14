
from django.contrib import admin
from django.urls import path, include
from manager import views
urlpatterns = [
    path('', views.mainadmin, name="mainadmin"),
    path('contact', views.contact, name="contact"),

    path('card', views.card, name="card"),
    path('Customers', views.Customers, name="customers"),
    path('update/<id>/', views.Update, name="update"),
    path('delete-appo/<id>/', views.delete_appo, name="delete_appo"),
]

# path('services', views.services, name="services"),
# path('doctors', views.doctors, name="doctors"),
# path('appointment', views.appointment, name="appointment"),
# path('faq', views.faq, name="faq"),
# path('testimonials', views.testimonials, name="testimonials"),
