from django.shortcuts import render
from django.urls import  reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .models import User
from .forms import RegisterForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        else:
            return render(response, 'registration/register.html', {'form' : form})
    else:
        form = RegisterForm()

        return render(response, 'registration/register.html', {'form' : form})

    return HttpResponseRedirect("/login/")