from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from blog.models import Post

class FieldsMixin:
    def dispatch(self, request, *args, **kwargs):
        # check the user's premissions
        if request.user.is_superuser or request.user.is_author:
            self.fields = [
                'title', 'thumbnail', 
                'slug', 'description', 
                'category', 'publish', 
                'is_special', 'status',
                ]
            # author field is only for superusers
            if request.user.is_superuser:
                self.fields.append('author')
        else:
            # raise error for non premissions users
            raise Http404('you can\'t access to this page !')
        
        return super().dispatch(request, *args, **kwargs)

class FormValidMixin:
    def form_valid(self, form):
        # check the user's premissions
        if self.request.user.is_superuser:
            # no edit
            form.save()
        else:
            # set the author and status parameters
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            # authors only can draft or investigation statues
            if self.obj.status != 'i':
                self.obj.status = 'd'
        
        return super().form_valid(form)


class AuthorAccessMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        # superusers always allow access
        if not request.user.is_superuser:
            # check the author of Post object
            post = get_object_or_404(Post, pk=pk)
            # the author can not edit the published posts !
            if post.author != request.user or post.status in ['p', 'i'] :
                raise Http404('you can\'t access to this page !')
        
        return super().dispatch(request, pk, *args, **kwargs)

class AuthorsAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        # redirect anonymous users to login page
        if not request.user.is_authenticated:
            return redirect('login')
        
        # only superusers and authors allow access
        if request.user.is_superuser or request.user.is_author:
            return super().dispatch(request, *args, **kwargs)
        # redirect to the profile page
        return redirect('account:profile')

class SuperUserMixin:
    def dispatch(self, request, *args, **kwargs):
        # only superusers allow access
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        
        raise Http404('you can\'t access to this page !')
        