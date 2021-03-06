from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm


# Create your views here.

def single_slug(request, single_slug):
    categories =[c.category_slug for c in TutorialCategory.objects.all()]
    # here we said that categories = the category slug for all objects in TutorialCategory
    if single_slug in categories:
        matching_series=TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        #here we are going to all objects in TutorialSeries and finding the tutorial_category which points to the TutorialCategory model
        # and by __ we are pointing to itself and saying that within that TutorialCategory's category slug
        
        series_urls={}

        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
        # here we are going to Tutorial object and tutorial_series in that object
        # the first tutorial_series points to TutorialSeries. The second one (after the __ ) points to the tutorial_series in TutorialSeries
        
        series_urls[m]= part_one.tutorial_slug
        return render(request,
                      "main/category.html",
                      context={"tutorial_series": matching_series, "part_ones": series_urls})



    tutorials =[t.tutorial_slug for t in Tutorial.objects.all()]
    
    if single_slug in tutorials:
        return HttpResponse(f"{single_slug} is a tutorial!!!")

    return HttpResponse(f"{single_slug} does not correspond to anything")


def homepage(request):
    return render(request = request,  
                        template_name="main/categories.html", 
                        context={'categories': TutorialCategory.objects.all()})

def register(request):
    if request.method=="POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'New Account Created :{username}') 
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.info(request, f'You are now logged in as {username}')
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            
            return render(request = request,
                        template_name = "main/register.html",
                        context={"form":form})

    form = NewUserForm
    return render(request,
                  "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request,"Logout Successful")
    return redirect("main:homepage")

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect("main:homepage")
            else: 
                messages.error(request,"Invalid username or password")
        else: 
                messages.error(request,"Invalid username or password")



         
    form=AuthenticationForm()
    return render (request,
                   "main/login.html",
                   {"form":form})