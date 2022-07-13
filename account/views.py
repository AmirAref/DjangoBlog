from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from blog.models import Post

# Create your views here.
class PostList(LoginRequiredMixin, ListView):
    queryset = Post.objects.all()
    template_name = 'registration/home.html'