from email.policy import default
from django.db import models
from autoslug import AutoSlugField

from django.urls import reverse, reverse_lazy
from taggit.managers import TaggableManager


class Person(models.Model):
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    age = models.PositiveSmallIntegerField("Возраст", default=0)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    title = models.CharField("Название", max_length=150)
    autor = models.CharField("Автор", blank=True, max_length=50)
    image = models.ImageField("Изображение", upload_to="images/")
    description = models.TextField("Описанеие")
    date = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True)
    tags = TaggableManager(blank=True)
    slug = AutoSlugField(populate_from='title', unique=True,
                         db_index=True, editable=True, blank=True)

    def get_absolute_url(self):
        return reverse("post_detail", args=(self.slug, ))

    def __str__(self) -> str:
        return self.title


class Mail(models.Model):
    mail = models.EmailField("Почта", unique=True)

    def __str__(self) -> str:
        return self.mail