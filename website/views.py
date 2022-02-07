import email
from email import message
from turtle import setundobuffer
from unicodedata import name
from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blog_details(request):
    return render(request, 'blog_details.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send Email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email;
            ['southcrr@gmail.com'], # to email
            fail_silently=False, # in production we would prbably change this to True
        )

        return render(request, 'contact.html', {'message_name' : message_name})

    else:
        return render(request, 'contact.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def service(request):
    return render(request, 'service.html', {})


