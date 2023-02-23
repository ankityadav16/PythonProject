from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('home/',views.UserHomeView.as_view(),name='home'),
    path('<username>/update',views.UserProfileUpdateView.as_view(),name='update'),
]
