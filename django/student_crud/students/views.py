from django.shortcuts import render

def index(request):
    return render(request,'students/index.html')

def about_us(request):
    return render(request,'students/about.html')

def services(request):
    return render(request,'students/services.html')

def contact(request):
    return render(request,'students/contact.html')

