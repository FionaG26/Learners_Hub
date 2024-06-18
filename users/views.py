from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'base.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
                                    
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            error = 'Invalid username or password. Please try again.'
            return render(request, 'users/login.html', {'error': error})
                                                                    
    return render(request, 'users/login.html')
                                                                    

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')
