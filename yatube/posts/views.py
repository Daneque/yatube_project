from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'posts/index.html'

    title = 'Последние обновления на сайте'

    context = {
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'

    title = 'Лев Толстой – зеркало русской революции.'

    context = {
        'title': title,
    }
    return render(request, template, context)
