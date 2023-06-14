from django.contrib import admin
# Register your models here.


from home.models import Contact, Appointment  # , Testimonials


admin.site.register(Contact)
admin.site.register(Appointment)
# admin.site.register(Testimonials)
