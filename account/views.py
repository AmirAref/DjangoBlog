from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .mixins import FieldsMixin, FormValidMixin, AuthorAccessMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from blog.models import Post

# Create your views here.
class PostList(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'
    
    def get_queryset(self) :
        # all posts for superuser
        if self.request.user.is_superuser:
            return Post.objects.all()
        else:
            # only the specific user's posts
            return Post.objects.filter(author=self.request.user)


class PostCreate(LoginRequiredMixin, FieldsMixin, FormValidMixin, CreateView):
    model = Post
    template_name = 'registration/post-create-update.html'

class PostUpdate(AuthorAccessMixin, FieldsMixin, FormValidMixin, UpdateView):
    model = Post
    template_name = 'registration/post-create-update.html'

class PostDelete(AuthorAccessMixin, FieldsMixin, FormValidMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('account:home')
    template_name = 'registration/post_confirm_delete.html'