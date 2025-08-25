from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def signup_view(request):
    """Handle user signup"""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            return redirect("users:profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    """Handle user login"""
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("users:profile")
    else:
        form = CustomAuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    """Handle logout"""
    logout(request)
    return redirect("users:login")


@login_required
def profile_view(request):
    """Simple profile page"""
    return render(request, "users/profile.html", {"user": request.user})
