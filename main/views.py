from os import remove
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib.auth import get_user
from taggit.models import Tag

from .models import Post
from .forms import PostForm


class PostsView(View):
    """Список постов"""

    def get(self, request):
        context = {
            "posts": Post.objects.all().order_by('-date'),
            "tags": Tag.objects.all()
        }
        return render(request, "main/index.html", context)


class PostDetailView(View):
    """Страница с постом"""

    def get(self, request, post_slug):
        return render(request, "main/post_detail.html", {'post': get_object_or_404(Post, slug=post_slug)})





class CRUD_PostView(View):
    """Создание поста"""

    def get(self, request):
        return render(request, "main/create_post.html")

    def create(request):
        post_form = PostForm()
        error = ""

        if request.method == "POST":  # проверяем то что метод именно POST
            form = PostForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                new_post = form.save(commit=False)
                # Добавление имени пользователя
                new_post.autor = get_user(request)
                new_post.save()
                return redirect("index.html")
            else:
                error = "Неверные данные формы!"

        data = {
            'post_form': post_form,
            'error': error,
        }

        return render(request, "main/create_post.html", data)

    def edit(request, post_title=''):
        post = get_object_or_404(Post, title=post_title)
        # Заполнение формы изменяемым постом
        post_form = PostForm(instance=post)
        error = ""

        if request.method == "POST":  # проверяем то что метод именно POST
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                new_post = form.save(commit=False)
                # Изменение слага
                new_post.slug = request.POST["title"]
                new_post.save()
                return redirect("../")
            else:
                error = "Неверные данные формы!"

        data = {
            'post_form': post_form,
            'error': error,
        }

        return render(request, "main/create_post.html", data)

    def delete(request, post):
        post = Post.objects.get(slug=post)
        remove(f"media/{post.image}")
        post.delete()
        return redirect('home')


class TagView(View):
    """Теги"""

    def get(self, request, tag_slug):
        tags = Tag.objects.filter(slug=tag_slug).values_list('name', flat=True)
        posts = Post.objects.filter(tags__name__in=tags)
        context = {
            'posts': posts,
        }
        return render(request, "main/show_tag.html", context)


class TagsView(View):
    """Теги"""

    def get(self, request):
        tags = Tag.objects.all()
        context = {
            'tags': tags,
        }
        return render(request, "main/tags.html", context)
