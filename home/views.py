from django.shortcuts import render, redirect, HttpResponse
from home.models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    User.objects.register(request.POST)
    return redirect('/')

def login(request):
    result = User.objects.athenticate(request.POST['email'], request.POST['password'])
    if result == False:
        messages.error(request, "Invalid Email/Password")
    else: 
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/success')
    return redirect('/')

def success(request):
    context = {
        'user' : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'success.html', context)