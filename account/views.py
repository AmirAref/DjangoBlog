from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .mixins import AuthorsAccessMixin, FieldsMixin, FormValidMixin, AuthorAccessMixin, SuperUserMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, PasswordChangeView
from blog.models import Post, Category
from .models import User
from .tokens import account_activation_token
from account.forms import ProfileForm, SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.conf import settings

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

class Register(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    
    def form_valid(self, form):
        # save the user object
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        # email parameters
        current_site = get_current_site(self.request)
        mail_subject = 'فعالسازی اکانت'
        message = "لینک فعالسازی حساب شما ارسال شد."
        from_email = settings.EMAIL_HOST_USER
        html_message = render_to_string('registration/account_activation.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        send_mail(
            subject=mail_subject,
            from_email=from_email,
            recipient_list=[to_email],
            message=message,
            html_message=html_message,
        )
        # show message
        return render(self.request, 'registration/auth_message.html', context={'step':'sent'})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # check user token
    if user is not None and account_activation_token.check_token(user, token):
        # activate the user
        user.is_active = True
        user.save()
        # show message
        return render(request, 'registration/auth_message.html', context={'step':'activated'})
    else:
        # invalid link
        # show message
        return render(request, 'registration/auth_message.html', context={'step':'failed'})


class CategoryList(SuperUserMixin, ListView):
    template_name = 'registration/category-list.html'
    model = Category
    
class CategoryCreate(SuperUserMixin, CreateView):
    model = Category
    fields = ['parent', 'title', 'slug', 'status', 'position']
    template_name = 'registration/category-create-update.html'

class CategoryUpdate(SuperUserMixin, UpdateView):
    model = Category
    fields = ['parent', 'title', 'slug', 'status', 'position']
    template_name = 'registration/category-create-update.html'

class CategoryDelete(SuperUserMixin, DeleteView):
    success_url = reverse_lazy('account:category')
    model = Category
    template_name = 'registration/category_confirm_delete.html'
