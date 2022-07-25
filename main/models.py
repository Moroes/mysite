from statistics import mode
from django.db import models
from datetime import date
from autoslug import AutoSlugField

from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import AbstractUser

class Person(models.Model):
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    age = models.PositiveSmallIntegerField("Возраст", default=0)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    title = models.CharField("Название", max_length=150)
    autor = models.ForeignKey(Person, on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="images/")
    description = models.TextField("Описанеие")
    date = models.DateField(
        "Дата добавления", auto_now_add=True, db_index=True)
    slug = AutoSlugField(populate_from='title', unique=True, db_index=True)
    def get_absolute_url(self):
        return reverse("post_detail", args=(self.slug, ))

    def __str__(self) -> str:
        return self.title


