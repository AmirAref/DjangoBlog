from django.urls import path, re_path
from .views import PostList, ArticleDetail, CategoryList

app_name = 'blog'
urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('page/<int:page>', PostList.as_view(), name="home"),
    path('article/<slug:slug>', ArticleDetail.as_view(), name="detail"),
    path('category/<slug:slug>', CategoryList.as_view(), name="category"),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name="category"),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)