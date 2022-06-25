from tabnanny import verbose
from django.db import models
from django.utils import timezone
from extensions.utils import jalali_convertor

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
    status = models.BooleanField(default=True, verbose_name="وضعیت نمایش")
    position = models.IntegerField(unique=True, verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی ها"
        ordering = ['position']
    
    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    STATUS_CHOICES = (
        ('p', 'منتشر شده'),
        ('d', 'پیش‌نویس'),
    )
    title = models.CharField(max_length=200, verbose_name='عنوان پست')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='لینک یکتا')
    description = models.TextField(verbose_name='توضیحات')
    category = models.ManyToManyField(Category)
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images', verbose_name='تصویر')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت انتشار')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        ordering = ['-publish']
    
    def jpublish(self):
        return jalali_convertor(self.publish)
    
    jpublish.short_description = publish.verbose_name

    def __str__(self) -> str:
        return self.title