from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileUpdateForm

def home(request):
    return render(request, 'home.html')

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

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Add your form handling logic here.
        return HttpResponseRedirect(reverse('contact'))
    return render(request, 'contact.html')

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

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Handle the subscription logic here
        # For example, save the email to the database or send a confirmation email
        return HttpResponse('Thank you for subscribing!')
    return render(request, 'home.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')  # Redirect to the profile page after update
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'form': form
    }
    return render(request, 'users/profile_update.html', context)
