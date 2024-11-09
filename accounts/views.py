from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.forms import CustomUserCreationForm


def register_request(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                messages.success(request, 'Registration successful!')
                return redirect('login')  # Registration successful, redirect to home
            else:
                messages.error(request, 'Authentication failed. Please try logging in.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_request(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')  # Başarılı giriş sonrası ana sayfaya yönlendirme
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'accounts/login.html', {'form': form})
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'accounts/login.html', {'form': form, "validation_error": "Something wrong!"})
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def logout_request(request):
    logout(request)
    return redirect('login')