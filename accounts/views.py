from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import registerUserForm
from django.contrib import messages
# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        form = registerUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('accounts:loginUser')
    
    else:
        form = registerUserForm()

    context = {
        'form': form
    }
    return render(request, "accounts/registration.html", context)

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request = request, data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password = password)
            if user is not None:
                login(request, user)
                return redirect('core:index')
        
            
            
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    if form.non_field_errors:
        print(form.non_field_errors())
    return render(request, "accounts/login.html", context)


def logoutUser(request):
    logout(request)

    return redirect('accounts:loginUser')

