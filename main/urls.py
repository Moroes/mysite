from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

 
urlpatterns = [
    path("", views.PostsView.as_view(), name='home'),
    path("create_post", views.CRUD_PostView.create, name='create_post'),
    path("<slug:post_slug>", views.PostDetailView.as_view(), name='post_detail'),
    path("tags/<tag_slug>", views.TagView.as_view(), name='tag'),
    path("tags/", views.TagsView.as_view(), name='tags'),
    path("<post>/delete", views.CRUD_PostView.delete, name='delete_post'),
    path("<post_title>/edit", views.CRUD_PostView.edit, name='edit_post'),
]