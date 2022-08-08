from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class SignUpView(CreateView):
    success_url = reverse_lazy('post-lists')
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'

# Create your views here.
