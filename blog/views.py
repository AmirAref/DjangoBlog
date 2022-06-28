from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Category, Post


# Create your views here.
def home(request, page=1):
    # make paginator object
    posts_list = Post.objects.published()
    paginator = Paginator(posts_list, 6)
    # get and display the specific page object
    page_object = paginator.get_page(page)
    contex = {
        'posts' : page_object,
    }
    return render(request, 'blog/home.html', contex)


def artcile_detail(request, slug):
    contex = {
        'post' : get_object_or_404(Post.objects.published(), slug=slug)
        }
    return render(request, 'blog/details.html', contex)

def category(request, slug, page=1):
    # variables
    category = get_object_or_404(Category, slug=slug, status=True)
    posts_list = category.posts.published()
    # make paginator object
    paginator = Paginator(posts_list, 6)
    # get and display the specific page object
    page_object = paginator.get_page(page)
    contex = {
        'category' : category,
        'posts' : page_object,
        }
    return render(request, 'blog/category.html', contex)