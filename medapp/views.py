from django.shortcuts import render, redirect
from medapp.models import *

# Create your views here.
def home (request):
    return render(request,'index.html')
def starter (request):
    return render(request,'starter-page.html')
def about (request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def doctors(request):
    return render(request,'doctors.html')
def department (request):
    return render(request,'departments.html')
def appoint (request):
    if request.method == "POST":
        myappointments=Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],
        )
        myappointments.save()
        return redirect('/show/')
    else:
        return render(request,'appointment.html')

def contact(request):
    if request.method == "POST":
        my_appointments=Contact(
        name = request.POST['name'],
        email = request.POST['email'],
        subject = request.POST['subject'],
        message = request.POST['message'],
        )
        my_appointments.save()
        return redirect('/contact/')
    else:
        return render(request,'contact.html')

def show (request):
    all = Appointment.objects.all()
    return render(request,'show.html',{'all':all})

def delete (request,id):
    deleteappointment = Appointment.objects.get(id=id)
    deleteappointment.delete()
    return redirect('/show/')
