## Описание:
Данный проект представляет собой социальную сеть "Yatube".
Аутентификация пользователей организована при помощи JWT-токенов.
Пользователи могут создавать посты и делать к ним комментарии.
Так же можно прикреплять фотографии к своим публикациям.
Можно подписываться на других пользователей, которые вам интересны и за чьими публикациями вы хотите следить.
В данном проекте используются следующие модели:
* **Group** - модель группы, содержащая поля _**title**_ (заголовок группы), **_slug_** (слаг группы) и **_description_** (описание группы).

* **Post** - модель поста, содержащая поля **_text_** (текст поста), **_pub_date_** (дата публикации), **_author_** (автор поста), **_image_** (изображение, необязательное поле) и **_group_** (группа, к которой относится пост).

* **Follow** - модель подписки, содержащая поля **_user_** (пользователь, который подписан) и **_following_** (пользователь, на которого подписаны).

* **Comment** - модель комментария, содержащая поля **_author_** (автор комментария), **_post_** (пост, к которому написан комментарий), **_text_** (текст комментария) и **_created_** (дата добавления комментария).


В файле **views.py** определены следующие представления (**viewsets**):

**PostViewSet** - представление для модели **_Post_**, предоставляющее операции CRUD (создание, чтение, обновление, удаление) для постов.

**GroupViewSet** - представление для модели **_Group_**, предоставляющее операцию чтения для групп.

**CommentViewSet** - представление для модели **_Comment_**, предоставляющее операции CRUD для комментариев.

**FollowViewSet** - представление для модели **_Follow_**, предоставляющее операции CRUD для подписок.

В файле **_serializers.py_** определены сериализаторы для преобразования объектов моделей в JSON и обратно. Каждый сериализатор соответствует одной из моделей и определяет поля, которые будут сериализованы.

## Как запустить проект:

**Клонировать репозиторий и перейти в него в командной строке:**
```
git clone https://github.com/Alnewage/api_final_yatube.git
```

```
cd api_final_yatube
```

**Cоздать и активировать виртуальное окружение:**
```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

**Установить зависимости из файла requirements.txt:**
```
pip install -r requirements.txt
```

**Выполнить миграции:**
```
python3 manage.py migrate
```

**Запустить проект:**
```
python3 manage.py runserver
```

## Примеры некоторых запросов к API:
**Регистрация пользователя:**
```
POST /api/v1/users/
```

**Получение токена:**
```
POST /api/v1/jwt/create/
```

**Обновление токена:**
```
POST /api/v1/jwt/refresh/
```

**Проверка JWT-токена:**
```
POST /api/v1/jwt/verify/
```

**Получение публикаций:**
```
GET /api/v1/posts/
```

**Создание публикаций:**
```
POST /api/v1/posts/
```

**Получение публикации по id:**
```
GET /api/v1/posts/{id}/
```

**Обновление публикации по id:**
Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
```
PUT /api/v1/posts/{id}/
```

**Частичное обновление публикации по id:** Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
```
PATCH /api/v1/posts/{id}/
```

**Удаление публикации по id:** Удалить публикацию может только автор публикации. Анонимные запросы запрещены.
```
DELETE /api/v1/posts/{id}/
```

**Получение всех комментариев к публикации:**
```
GET /api/v1/posts/{post_id}/comments/
```

**Добавление нового комментария к публикации:** Анонимные запросы запрещены.
```
POST /api/v1/posts/{post_id}/comments/
```

**Получение комментария к публикации по id:**
```
GET /api/v1/posts/{post_id}/comments/{id}/
```

**Обновление комментария к публикации по id:** Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
```
PUT /api/v1/posts/{post_id}/comments/{id}/
```

**Частичное обновление комментария к публикации по id:** Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
```
PATCH /api/v1/posts/{post_id}/comments/{id}/
```

**Удаление комментария к публикации по id:** Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
```
DELETE /api/v1/posts/{post_id}/comments/{id}/
```

**Получение списка доступных сообществ:**
```
GET /api/v1/groups/
```

**Получение информации о сообществе по id:**
```
GET /api/v1/groups/{id}/
```

**Возвращает все подписки пользователя, сделавшего запрос:** Анонимные запросы запрещены.
```
GET /api/v1/follow/
```

**Подписать на другого пользователя:** Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.
```
POST /api/v1/follow/
```
