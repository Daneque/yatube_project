from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Hello! In future here will be the main page'
                        'of innovation social network YATUBE!')


def group_posts(request, slug):
    return HttpResponse(f'Group page and your slug:{slug}')


