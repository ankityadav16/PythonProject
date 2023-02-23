from django.shortcuts import render
from django.views.generic import View,CreateView
from .forms import UserSignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import LoginForm

# Create your views here.
class SignUpView(CreateView):
    form_class = UserSignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm