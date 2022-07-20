from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from account.mixins import AuthorAccessMixin
from account.models import User
from .models import Category, Post


# Create your views here.
class PostList(ListView):
    queryset = Post.objects.published()
    paginate_by = 6

class ArticleDetail(DetailView):
    # display the detial page of any article (post) by slug
    def get_object(self) :
        slug = self.kwargs['slug']
        post = get_object_or_404(Post.objects.published(), slug=slug)
        # save the ip address for this post
        ip_address = self.request.user.ip_address
        if not ip_address in post.hits.all():
            post.hits.add(ip_address)
        
        return post

class ArticlePreview(AuthorAccessMixin, DetailView):
    # display the detial page of any article (post) by slug
    def get_object(self) :
        pk = self.kwargs['pk']
        return get_object_or_404(Post, pk=pk)


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

class AuthorList(ListView):
    paginate_by = 6
    template_name = 'blog/author_list.html'
    
    def get_queryset(self):
        # display the artciles list of the category
        self.author = get_object_or_404(User, username=self.kwargs['username'])
        return self.author.posts.published()
    
    def get_context_data(self, **kwargs):
        # add the author to the contex
        contex = super().get_context_data(**kwargs)
        contex['author'] = self.author
        return contex