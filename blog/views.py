from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def home(request):
    contex = {
        'posts' : Post.objects.filter(status='p'),
    }
    return render(request, 'blog/home.html', contex)


def artcile_detail(request, slug):
    contex = {
        'post' : get_object_or_404(Post, slug=slug, status='p')
        }
    return render(request, 'blog/details.html', contex)