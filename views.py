from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
import random



def demofunction(request):
    return HttpResponse("PFSD SDP PROJECT")

def demofunction1(request):
    return HttpResponse("<h3> PROJECT </h3>")

def demofunction2(request):
    return HttpResponse("<font color='orange'> SERVICE MANAGEMENT SYSTEM </font>")

def homefunction(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"about.html")

def loginfunction(request):
    return render(request,"login.html")

def registerfunction(request):
    return render(request,"register.html")


def contactfunction(request):
    return render(request,"contact.html")


def generate_otp():
    return str(random.randint(1000, 9999))



def send_otp_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = generate_otp()


        otp_storage[email] = otp
        otp_storage = {}

        subject = 'OTP Verification'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'validate_otp.html')
    return render(request, 'send_otp.html')

def validate_otp(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_otp = request.POST['otp']


        stored_otp = otp_storage.get(email)

        if user_otp == stored_otp:

            return redirect('attendance_list')
        else:
            return redirect('validate_otp',msg='InValid OTP')

    return render(request, 'validate_otp.html')