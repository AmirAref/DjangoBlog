from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q

from account.mixins import AuthorAccessMixin
from account.models import User
from .models import Category, Post


# Create your views here.
class PostList(ListView):
    queryset = Post.objects.published()
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.active()
        return context
    

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.active()
        return context

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
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context["categories"] = Category.objects.active()
        return context

class AuthorList(ListView):
    paginate_by = 6
    template_name = 'blog/author_list.html'
    
    def get_queryset(self):
        # display the artciles list of the category
        self.author = get_object_or_404(User, username=self.kwargs['username'])
        return self.author.posts.published()
    
    def get_context_data(self, **kwargs):
        # add the author to the contex
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        context["categories"] = Category.objects.active()
        return context


class SearchList(ListView):
    paginate_by = 6
    template_name = 'blog/search_list.html'
    
    def dispatch(self, request, *args, **kwargs):
        # check empty query field
        query = request.GET.get('q')
        if not query:
            return redirect('blog:home')

        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        # get post that their title or description contains the query 
        self.query = self.request.GET.get('q')
        posts = Post.objects.published().filter(Q(title__icontains=self.query) | Q(description__icontains=self.query))
        return posts
    
    def get_context_data(self, **kwargs):
        # add the author to the contex
        context = super().get_context_data(**kwargs)
        context['query'] = self.query
        context["categories"] = Category.objects.active()
        return context