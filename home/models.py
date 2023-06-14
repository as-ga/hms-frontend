from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    # user = models.ForeignKey(User, related_name="user_bookings",
    #                          on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    # user = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=(
        ('Male', 'Male'), ('Female', 'Female')))
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    address1 = models.TextField()
    address2 = models.TextField()
    appodate = models.DateField()
    appotime = models.CharField(max_length=100)
    doctor = models.TextField()

    date = models.DateField()

    def __str__(self):
        return self.name


# class Testimonials(models.Model):
#     user = models.ForeignKey(
#         User, related_name="user_bookings", on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     phone = models.CharField(max_length=12)
#     message = models.TextField()
#     date = models.DateField()

    # def __str__(self):
    #     return self.name
