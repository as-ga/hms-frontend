from home.models import *

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User


def mainadmin(request):
    appo = Appointment.objects.all()
    context = {
        'appo': appo,
        'page': "Manager"
    }
    return render(request, 'manager/admin.html', context)


def Update(request, id):
    queryset = Appointment.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        appodate = request.POST.get('appodate')
        appotime = request.POST.get('appotime')
        doctor = request.POST.get('doctor')

        queryset.name = name
        queryset.gender = gender
        queryset.phone = phone
        queryset.appodate = appodate
        queryset.appotime = appotime
        queryset.doctor = doctor

        queryset.save()
        return redirect('/manager/')

    context = {
        'appo': queryset,
        'page': "Update"
    }
    return render(request, 'manager/update.html', context)


def delete_appo(request, id):
    appo = Appointment.objects.get(id=id)
    appo.delete()
    return redirect('/manager/')


def card(request):
    return render(request, 'manager/card.html')


def Customers(request):
    return render(request, 'manager/Customers.html')


def contact(request):
    # if request.user.is_anonymous:
    #     return redirect('/user/login')
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     message = request.POST.get('message')
    #     print(name, email, phone, message)
    #     contact = Contact(name=name, email=email, phone=phone,
    #                       message=message, date=datetime.today())
    #     contact.save()
    #     if contact is not None:
    #         messages.warning(request, ' Your Messages Send')
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # messages.success(request, 'Your messages has been sent!')

    return render(request, 'pages/contact.html')
