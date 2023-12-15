from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import loginForm


def login_view(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            person = authenticate(request, email=email, password=password)
            if person is not None:
                login(request, person)
                # Redirect to your dashboard or any desired URL
                if person.is_superuser:
                    return redirect('/admin/')
                return redirect('dashboard')
            else:
                # Handle invalid login
                form.add_error(None, 'Invalid email or password')
    else:
        form = loginForm()

    return render(request, 'login.html', {'form': form})

def dashboard_view(request):
    return HttpResponse("this is the dashboard page")


def newticket_view(request):
    return HttpResponse("This is the newticket page")