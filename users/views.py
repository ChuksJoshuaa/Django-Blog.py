from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django import forms

from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import FormView
# Create your views here.
from .forms import Rawuserform, UserUpdateForm, ProfileUpdateForm


def user_registerview(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = Rawuserform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! You are now able to log in")
            return redirect('user_login')

    else:
        form = Rawuserform()
    context = {
        "form": form
    }
    return render(request, "user_register.html", context)

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except:
        profile = Profile(user=request.user)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=profile)
        if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request, f"Your account has been Updated!")
           return redirect('user_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user_profile.html', context)



