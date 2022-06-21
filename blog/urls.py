from django.urls import path, re_path
from .views import home, artcile_detail

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    re_path(r'article/(?P<slug>[-\w]+)', artcile_detail, name="detail")
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)