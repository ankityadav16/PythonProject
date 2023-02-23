from django.views.generic import TemplateView
from django.shortcuts import redirect
from user.views import UserHomeView

class Homepage(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user:home')

class Testpage(TemplateView):
    template_name = 'test.html'

class Thankspage(TemplateView):
    template_name = 'thanks.html'