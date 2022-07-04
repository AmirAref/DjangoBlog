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

class CategoryList(ListView):
    paginate_by = 6
    template_name = 'blog/category_list.html'
    
    def get_queryset(self):
        # display the artciles list of the category
        slug = self.kwargs['slug']
        self.category = get_object_or_404(Category.objects.active(), slug=slug)
        return self.category.posts.published()
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['category'] = self.category
        return contex