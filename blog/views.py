from django.shortcuts import render, get_object_or_404
from .models import Category, Post


# Create your views here.
def home(request):
    contex = {
        'posts' : Post.objects.published(),
        'categories' : Category.objects.filter(status=True),
    }
    return render(request, 'blog/home.html', contex)


def artcile_detail(request, slug):
    contex = {
        'post' : get_object_or_404(Post.objects.published(), slug=slug)
        }
    return render(request, 'blog/details.html', contex)

def category(request, slug):
    contex = {
        'category' : get_object_or_404(Category, slug=slug, status=True)
        }
    return render(request, 'blog/category.html', contex)