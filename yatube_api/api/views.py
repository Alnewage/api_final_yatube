from django.shortcuts import get_object_or_404

from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post

from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """
        ViewSet для модели Post.

        Атрибуты:
            queryset (QuerySet): QuerySet для получения всех постов из БД.
            serializer_class (Serializer): Сериализатор для модели Post.
            pagination_class (Pagination): Класс пагинации для списка постов.
            permission_classes (tuple): Кортеж классов разрешений
                для управления доступом к представлению.
        """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        """
        Выполняет операцию создания поста.
        """
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для модели Group.

    Атрибуты:
        queryset (QuerySet): QuerySet для получения всех групп из БД.
        serializer_class (Serializer): Сериализатор для модели Group.
        permission_classes (tuple): Кортеж классов разрешений для управления
            доступом к представлению.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Comment.

    Атрибуты:
        serializer_class (Serializer): Сериализатор для модели Comment.
        lookup_url_kwarg (str): Имя URL-параметра для поиска комментариев.
        permission_classes (tuple): Кортеж классов разрешений для управления
            доступом к представлению.
    """
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'
    permission_classes = (IsOwnerOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        """
        Возвращает:
            QuerySet: Комментарии, относящиеся к определенному посту.
        """
        self.post = self.get_post()
        return self.post.comments.all()

    def perform_create(self, serializer):
        """
        Выполняет операцию создания комментария.
        """
        post = self.get_post()
        serializer.save(author=self.request.user,
                        post=post, )

    def perform_update(self, serializer):
        """
        Выполняет операцию обновления комментария.
        """
        serializer.save(author=self.request.user,
                        post=self.post, )


class FollowViewSet(viewsets.ModelViewSet):
    """ ViewSet для модели Follow.

    Атрибуты:
        serializer_class (Serializer): Сериализатор для модели Follow.
        filter_backends (tuple): Кортеж классов фильтрации для поиска подписок.
        search_fields (tuple): Кортеж полей, по которым производится поиск
            подписок.
    """
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """
        Определяет QuerySet для получения подписок пользователя.
        """
        return self.request.user.following.all()

    def perform_create(self, serializer):
        """
        Выполняет операцию создания подписки.
        """
        serializer.save(user=self.request.user)
