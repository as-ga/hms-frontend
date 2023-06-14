from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
from home.models import Contact, Appointment  # , Testimonials
# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    if request.user.is_anonymous:
        return redirect('/user/login')
    return redirect('/')


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')


def doctors(request):
    return render(request, 'pages/doctors.html')


def appointment(request):
    if request.user.is_anonymous:
        return redirect('/user/login')
    if request.method == 'POST':
        # print(appointment())
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        appodate = request.POST.get('appodate')
        appotime = request.POST.get('appotime')
        doctor = request.POST.get('doctor')
        appointment = Appointment(name=name, gender=gender, phone=phone, email=email,
                                  address1=address1, address2=address2, appodate=appodate, appotime=appodate, doctor=doctor, date=datetime.today())
        appointment.save()
        if appointment is not None:
            messages.warning(request, ' Your Appointment Book Suscesfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'pages/appointment.html')


def faq(request):
    return render(request, 'pages/faq.html')


def testimonials(request):
    # if request.user.is_anonymous:
    #     return redirect('/user/login')
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     message = request.POST.get('message')
    #     print(name, email, phone, message)
    #     testimonials = Testimonials(user=request.user, name=name, email=email, phone=phone,
    #                                 message=message, date=datetime.today())
    #     testimonials.save()
    #     if testimonials is not None:
    #         messages.warning(request, ' Your Messages Send')
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'pages/testimonials.html')


def contact(request):
    # if request.user.is_anonymous:
    # return redirect('/user/login')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # print(name, email, phone, message)
        contact = Contact(name=name, email=email, phone=phone,
                          message=message, date=datetime.today())
        contact.save()
        if contact is not None:
            messages.warning(request, ' Your Messages Send')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        # messages.success(request, 'Your messages has been sent!')

    return render(request, 'pages/contact.html', {
        'data': Contact.objects.all()
    })
