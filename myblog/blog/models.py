from django.db import models
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):  # ТБ: blog_post
    # id - авто. создание

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    title = models.CharField(
        max_length=32,
        verbose_name='Название'
    )

    slug = models.SlugField(
        unique=True,
        verbose_name='Символьный ID'
    )

    text = models.TextField(
        verbose_name='Тело поста'
    )

    published = models.BooleanField(
        default=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
