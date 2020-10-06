from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.



def homepage(request):
    return render(request = request,  
                        template_name="main/home.html", 
                        context={'tutorials': Tutorial.objects.all})

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    if request.method=="POST":
        if request.POST.get('submit') == 'sign_in':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                user=form.save()
                username=form.cleaned_data.get('username')
                messages.success(request, f'New Account Created :{username}') 

                username = form.cleaned_data.get('username')
                login(request, user)
                return redirect("main:homepage")
        elif request.POST.get('submit') == 'sign_up':
             if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/home')

        else:
            for msg in form.error_messages:
                messages.error(request,f'{msg}: form.error_messages[msg]')

    form=UserCreationForm
    return render(request = request,
                  template_name="main/register.html",
                  context={'form': form})
