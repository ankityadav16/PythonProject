from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

class WebsiteView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("user:home"))
        return super().get(request, *args, **kwargs)

class AboutpageView(TemplateView):
    template_name = 'about.html'