# posts/urls.py
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [

    # Если URL - пустая строка, вызовется функция index()
    path('', views.index, name='index'),

    path('group/<slug:slug>/', views.group_posts, name='group_posts'),

]
