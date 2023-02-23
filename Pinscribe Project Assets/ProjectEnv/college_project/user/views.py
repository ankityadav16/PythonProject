from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

from django.urls  import reverse,reverse_lazy
from django.views import generic
from posts.models import Post
from .models import Profile
from django import forms
from .forms import ProfileUpdateForm
from django.contrib.auth.models import User

class UserHomeView(generic.ListView,LoginRequiredMixin):
    model = Post
    template_name = 'user/user_home.html'


class UserProfileUpdateView(generic.UpdateView,LoginRequiredMixin):
    model = Profile
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('user:home')
    template_name = 'user/update_user_profile.html'