from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from django import forms
class Form(forms.Form):
    message_name = forms.CharField()
    message_email = forms.CharField()
    message = forms.CharField()

def home(request):
    return render(request, 'index.html', {})

def contact(request):
    if request.method == 'GET':
        form = Form()
        return render(request, 'contact.html', {'form': form})

    if request.method == 'POST':
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        #print(message_name, message, message_email)

        #send an email
        send_mail(
            'Hello world ' + message_name,
            message,
            message_email,
            ['raulbaciulescu@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'contact.html', {'message_name': message_name})