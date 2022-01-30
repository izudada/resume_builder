from django.shortcuts import render
from django.urls import  reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, TemplateView

from .models import Profile


class UserProfile(LoginRequiredMixin, TemplateView):
    model = Profile
    fields = '__all__'
    template_name = 'resume/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Profile.objects.all()
        return context
