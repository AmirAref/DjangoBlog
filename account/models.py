from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    is_author = models.BooleanField(default=False, verbose_name="وضعیت نویسندگی")
    special_subscription = models.DateTimeField(default=timezone.now, verbose_name='اشتراک ویژه')

    # boolean field of special subscription
    def is_special_user(self):
        if self.special_subscription > timezone.now():
            return True
        return False
    is_special_user.boolean = True
    is_special_user.short_description = "وضعیت کاربر ویژه"
