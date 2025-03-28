from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.
def registration_list(request):
    return render(request,"student_registration/registration_list.html")

def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
            form = RegistrationForm()    
    return render(request,"student_registration/registration_form.html",{'form':form})

def view_registration(request):
    return render(request,"student_registration/view_registration.html")

def delete_registration(request):
    return render(request,"student_registration/delete_registration.html")