from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.TextField()
    slug = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    # Создает текстовое поле неограниченной длины.
    text = models.TextField()

    # Создает поле даты публикаций.
    pub_date = models.DateTimeField(auto_now_add=True)

    # Создает ссылку на модель User
    author = models.ForeignKey(
        User,
        # если в User удалить пользователя, то удалятся все его записи
        on_delete=models.CASCADE,
        # у объекта User появится поле posts, хранящее ссылки
        # на все посты автора
        related_name='posts'
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
