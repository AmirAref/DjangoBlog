from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .mixins import AuthorsAccessMixin, FieldsMixin, FormValidMixin, AuthorAccessMixin, SuperUserMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, PasswordChangeView
from blog.models import Post
from .models import User
from account.forms import ProfileForm

# Create your views here.
class PostList(AuthorsAccessMixin, ListView):
    template_name = 'registration/home.html'
    
    def get_queryset(self) :
        # all posts for superuser
        if self.request.user.is_superuser:
            return Post.objects.all()
        else:
            # only the specific user's posts
            return Post.objects.filter(author=self.request.user)


class PostCreate(AuthorsAccessMixin, FieldsMixin, FormValidMixin, CreateView):
    model = Post
    template_name = 'registration/post-create-update.html'

class PostUpdate(AuthorAccessMixin, FieldsMixin, FormValidMixin, UpdateView):
    model = Post
    template_name = 'registration/post-create-update.html'

class PostDelete(SuperUserMixin, FieldsMixin, FormValidMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('account:home')
    template_name = 'registration/post_confirm_delete.html'

class Profile(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('account:profile')
    template_name = 'registration/profile.html'
    
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    
    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update(
            {'user' : self.request.user}
        )
        return kwargs

class Login(LoginView):
    def get_success_url(self):
        user = self.request.user
        # check user premission type
        if user.is_superuser or user.is_author:
            # home page
            return reverse_lazy('account:home')
        else:
            # profile page
            return reverse_lazy('account:profile')

class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')