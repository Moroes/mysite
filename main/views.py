from datetime import date
from turtle import pos, title
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from .models import Person, Post
from .forms import PostForm

# Create your views here.


class PostsView(View):
    """Список постов"""

    def get(self, request):
        return render(request, "main/index.html", {"posts": Post.objects.all()})


class PostDetailView(View):
    """Страница с постом"""

    def get(self, request, post_slug):
        print(get_object_or_404(Post, slug=post_slug))
        return render(request, "main/post_detail.html", {'post': get_object_or_404(Post, slug=post_slug)})


class CreatePostView(View):
    """Создание поста"""

    def get(self, request):
        return render(request, "main/create_post.html")

    def create(request):
        post_form = PostForm()
        error = ""

        if request.method == "POST":  # проверяем то что метод именно POST
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("index.html")
            else:
                error = "Неверные данные формы!"

        data = {
            'post_form': post_form,
            'error': error,
        }

        return render(request, "main/create_post.html", data)
