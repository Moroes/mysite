from django.contrib import admin

from .models import Post, Person, Mail

# Register your models here.
admin.site.register(Post)
admin.site.register(Person)
admin.site.register(Mail)
    