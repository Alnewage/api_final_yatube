"""
Данный модуль содержит сериализаторы для преобразования объектов
моделей Django в JSON и обратно.
"""

import base64

from django.core.files.base import ContentFile

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class Base64ImageField(serializers.ImageField):
    """
    Пользовательское поле сериализатора для обработки изображений
    в формате base64.
    """

    def to_internal_value(self, data):
        """
        Преобразует значение изображения из формата base64 в объект файла.
        """
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext, )

        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели `Post`.
    """
    author = SlugRelatedField(slug_field='username', read_only=True, )
    image = Base64ImageField(required=False, allow_null=True)
    pub_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M",
                                         read_only=True, )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group',)


class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели `Group`.
    """

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели `Comment`.
    """
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username', )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created',)
        read_only_fields = ('post', 'created',)


class FollowSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели `Follow`.
    """
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True, )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all(), )

    class Meta:
        model = Follow
        fields = ('user', 'following',)

    def validate(self, data):
        user = self.context['request'].user
        # Проверяем, подписывается ли пользователь сам на себя.
        if user == data['following']:
            raise serializers.ValidationError('Нельзя подписаться на себя')
        # Проверяем, существует ли уже данная подписка в БД.
        if Follow.objects.filter(
            user=user,
            following=data['following']
        ).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого автора')
        return data
