"""
Данный модуль содержит модели, которые используются в приложении yatube_api.
"""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        help_text='Заголовок группы',
        verbose_name='Заголовок группы',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text='Слаг группы',
        verbose_name='Слаг группы',
    )
    description = models.TextField(
        help_text='Описание группы',
        verbose_name='Описание группы',
    )


class Post(models.Model):
    text = models.TextField(
        help_text='Текст поста',
        verbose_name='Текст поста',
    )
    pub_date = models.DateTimeField(
        help_text='Дата публикации',
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='Автор поста',
        verbose_name='Автор поста',
        related_name='posts',
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        help_text='Изображение',
        verbose_name='Изображение',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='posts',
        blank=True,
        null=True,
        help_text='Группа',
        verbose_name='Группа',
    )

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        help_text='Кто подписан',
        verbose_name='Кто подписан',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers',
        help_text='На кого подписан',
    )


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        help_text='Автор комментария',
        verbose_name='Автор комментария',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост',
        help_text='Пост',
    )
    text = models.TextField(
        help_text='Текст комментария',
        verbose_name='Текст комментария',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text='Дата добавления',
        verbose_name='Дата добавления',
    )
