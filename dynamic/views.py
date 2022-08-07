from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'index.html',{'posts':posts})

def smart(request):
    
    return render(request,'smart.html')

def digital(request):
    
    return render(request,'digital.html')

def convenient(request):
    
    return render(request,'convenient.html')

def safe(request):
    
    return render(request,'safe.html')

def sustainable(request):
    
    return render(request,'sustainable.html')

def access_control(request):
    
    return render(request,'access_control.html')

def availability(request):
    
    return render(request,'availability.html')

def digital_dashboard(request):
    
    return render(request,'digital_dashboard.html')

def mobile_application(request):
    
    return render(request,'mobile_application.html')

def guidance(request):
    
    return render(request,'guidance.html')

# Create your views here.
