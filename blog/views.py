from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Category, Post


# Create your views here.
class PostList(ListView):
    queryset = Post.objects.published()
    paginate_by = 6

class ArticleDetail(DetailView):
    # display the detial page of any article (post) by slug
    def get_object(self) :
        slug = self.kwargs['slug']
        return get_object_or_404(Post.objects.published(), slug=slug)

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