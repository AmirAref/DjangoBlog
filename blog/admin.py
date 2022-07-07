from django.contrib import admin, messages
from .models import Post, Category
from django.utils.translation import ngettext

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = ('status', )
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title', )}
    actions = ('make_active', 'make_inactive', )
    
    # make the posts published action
    @admin.action(description="فعال کردن")
    def make_active(self, request, queryset):
        updated = queryset.update(status=True)
        # alert message
        self.message_user(request, ngettext(
            '%d دسته‌بندی با موفقیت فعال شد.', #singular
            '%d دسته‌بندی با موفقیت فعال شدند.', #plural
            updated,
        ) % updated, messages.SUCCESS)

    # make the posts draft action
    @admin.action(description="غیرفعال کردن")
    def make_inactive(self, request, queryset):
        updated = queryset.update(status=False)
        # alert message
        self.message_user(request, ngettext(
            '%d دسته‌بندی با موفقیت غیرفعال شد.', #singular
            '%d دسته‌بندی با موفقیت غیرفعال شدند.', #plural
            updated,
        ) % updated, messages.SUCCESS)

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug', 'jpublish', 'status', 'caregoty_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug' : ('title', )}
    ordering = ('status', '-publish')
    actions = ('make_published', 'make_draft', )

    def caregoty_to_str(self, obj):
        # convert the categories list to the string
        return ", ".join(map(lambda x : x.title, obj.category.active() ))
    caregoty_to_str.short_description = "دسته بندی"
    
    # make the posts published action
    @admin.action(description="انتشار")
    def make_published(self, request, queryset):
        updated = queryset.update(status='p')
        # alert message
        self.message_user(request, ngettext(
            '%d مقاله با موفقیت منتشر شد.', #single
            '%d مقاله با موفقیت منتشر شدند.', #plural
            updated,
        ) % updated, messages.SUCCESS)

    # make the posts draft action
    @admin.action(description="پیش‌نویس")
    def make_draft(self, request, queryset):
        updated = queryset.update(status='d')
        # alert message
        self.message_user(request, ngettext(
            '%d مقاله با موفقیت پیش‌نویس شد.', #single
            '%d مقاله با موفقیت پیش‌نویس شدند.', #plural
            updated,
        ) % updated, messages.SUCCESS)


admin.site.register(Post, PostAdmin)