from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post


# Create your views here.
def home(request):
    contex = {
        'posts' : Post.objects.filter(status='p').order_by('-publish'),
    }
    return render(request, 'blog/home.html', contex)


def artcile_detail(request, slug):
    contex = {'post' : Post.objects.get(slug=slug)}
    return render(request, 'blog/details.html', contex)