from django.urls import path, re_path
from .views import home, artcile_detail, category

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('page/<int:page>', home, name="home"),
    path('article/<slug:slug>', artcile_detail, name="detail"),
    path('category/<slug:slug>', category, name="category"),
    path('category/<slug:slug>/page/<int:page>', category, name="category"),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)