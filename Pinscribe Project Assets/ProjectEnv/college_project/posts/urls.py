from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('new',views.CreatePost.as_view(),name='create'),
    path('by/<username>',views.UserPosts.as_view(),name='for_user'),
    path('by/<username>/<pk>',views.PostDetail.as_view(),name='single'),
]
