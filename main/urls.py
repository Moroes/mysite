from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

 
urlpatterns = [
    path("", views.PostsView.as_view(), name='home'),
    path("index.html", views.PostsView.as_view(), name='index'),
    path("create_post.html", views.CreatePostView.create, name='create_post'),
    path("<slug:post_slug>", views.PostDetailView.as_view(), name='post_detail')

    # path("<int:pk>/", views.MovieDetailView.as_view())
]