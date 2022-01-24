from django.shortcuts import render
from django.urls import  reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from .models import User
from .forms import RegisterForm


class UserCreateView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = "registration/register.html"

    def form_valid(self, form):
        return super(UserCreateView, self).form_valid(form)