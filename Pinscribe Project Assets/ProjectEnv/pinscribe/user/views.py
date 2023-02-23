from django.shortcuts import render
from django.views.generic import TemplateView,ListView

# Create your views here.
class UserHomepageView(TemplateView):
    template_name = 'user/home.html'