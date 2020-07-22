from django.shortcuts import render, redirect
from home.models import User

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    User.objects.register(request.POST)
    return redirect('/')
