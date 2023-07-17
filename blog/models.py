from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from account.models import User
from extensions.utils import jalali_convertor
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from star_ratings.models import Rating

# create your managers here
class PostManager(models.Manager):
    def published(self):
        # only published posts
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        # display only active categories
        return self.filter(status=True)


# create your models here
class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='آدرس آی‌پی')

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name='دسته‌بندی مادر')
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
    status = models.BooleanField(default=True, verbose_name="وضعیت نمایش")
    position = models.IntegerField(unique=True, verbose_name="جایگاه")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی ها"
        ordering = ['parent__id', 'position']

    def __str__(self) -> str:
        return self.title

    # change objects Manager
    objects = CategoryManager()
    
    
    # redirect url after created a object of this model
    def get_absolute_url(self):
        return reverse('account:category')

class Post(models.Model):
    STATUS_CHOICES = (
        ('p', 'منتشر شده'), #deraft
        ('d', 'پیش‌نویس'),  # published
        ('i', 'در حال بررسی'), # investigation
        ('r', 'رد شده'), # rejected
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='posts', verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name='عنوان پست')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='لینک یکتا')
    description = models.TextField(verbose_name='توضیحات')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='posts')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images', verbose_name='تصویر')
    is_special = models.BooleanField(default=False, verbose_name="مقاله ویژه")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت انتشار')
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress, blank=True, through='PostHit', related_name='posts', verbose_name='بازدیدها')
    ratings = GenericRelation(Rating)

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        ordering = ['-publish']

    # return jalali version of published date
    def jpublish(self):
        return jalali_convertor(self.publish)

    jpublish.short_description = publish.verbose_name
    
    # display the catories list as a string
    def category_to_str(self):
        # convert the categories list to the string
        return ", ".join(map(lambda x : x.title, self.category.active() ))
    category_to_str.short_description = "دسته بندی"
    
    # thumbnail little size tag (to dosplay in admin panel)
    def thumbnail_tag(self):
        return format_html(f'<img width=90 style="border-radius:5px" src={self.thumbnail.url}>')
    thumbnail_tag.short_description = thumbnail.verbose_name

    # redirect url after created a object of this model
    def get_absolute_url(self):
        return reverse('account:home')
    
    def __str__(self) -> str:
        return self.title

    # change objects Manager
    objects = PostManager()


class PostHit(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)