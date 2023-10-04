from django.urls import include, path

from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

# Создание экземпляра маршрутизатора
router_v1 = routers.DefaultRouter()

# Регистрация представлений (viewsets) в маршрутизаторе
router_v1.register(r'posts', PostViewSet, basename='posts', )
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments', )
router_v1.register(r'groups', GroupViewSet, basename='groups', )
router_v1.register(r'follow', FollowViewSet, basename='follow', )

urlpatterns = [
    # Подключение маршрутов роутера.
    path('', include(router_v1.urls), ),

    # Подключение URL-маршрутов для работы с токенами (djoser).
    path('', include('djoser.urls.jwt'), ),
]
