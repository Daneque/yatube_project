from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Create your views here.
def index(request):

    posts = Post.objects.order_by('-pub_date')[:10]

    title = 'Последние обновления на сайте'

    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    template = 'posts/group_list.html'

    group = get_object_or_404(Group, slug=slug)

    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

    title = f'Записи сообщества {slug}'

    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)
