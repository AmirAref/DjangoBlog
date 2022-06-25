from unicodedata import category
from django.contrib import admin
from .models import Post, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = ('status', )
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title', )}


admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status', 'caregoty_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug' : ('title', )}
    ordering = ('status', '-publish')
    
    def caregoty_to_str(self, obj):
        # convert the categories list to the string
        return ", ".join(map(lambda x : x.title, obj.category.all() ))
    caregoty_to_str.short_description = "دسته بندی"


admin.site.register(Post, PostAdmin)