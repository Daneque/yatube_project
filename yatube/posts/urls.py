# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [

    # Если URL - пустая строка, вызовется функция index()
    path('', views.index),

    path('group/<slug:slug>/', views.group_posts),

]
