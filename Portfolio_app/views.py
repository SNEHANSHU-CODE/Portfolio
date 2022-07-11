from django.shortcuts import render , redirect
from Portfolio_app.models import ContactUs
# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = ContactUs (name = name , email = email , subject = subject , message = message)
        contact.save()
        return render(request,'submit.html')
    else:
        return render(request,'index.html')

