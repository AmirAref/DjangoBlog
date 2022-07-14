from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# write your models admins here.
UserAdmin.fieldsets[2][1]['fields'] =  (
    'is_active', 
    'is_staff', 
    'is_superuser', 
    'is_author',
    'special_subscription',
    'groups', 
    'user_permissions'
    )

UserAdmin.list_display += ('is_author', 'is_special_user', )

# Register your models here.

admin.site.register(User, UserAdmin)