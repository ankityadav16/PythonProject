from django.urls import path
from .views import UserHomepageView

app_name = 'user'

urlpatterns = [
    path('',UserHomepageView.as_view(),name='home'),
]
