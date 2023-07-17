from django.urls import path
from .views import (
    PostList,
    PostCreate,
    PostUpdate,
    PostDelete,
    Profile,
    CategoryCreate,
    CategoryList,
    CategoryUpdate,
    CategoryDelete,
    )

app_name = 'account'

urlpatterns = [
    path('profile/', Profile.as_view(), name='profile'),  
    path('', PostList.as_view(), name='home'),   
    path('article/create', PostCreate.as_view(), name='post-create'),
    path('article/update/<int:pk>', PostUpdate.as_view(), name='post-update'),
    path('article/delete/<int:pk>', PostDelete.as_view(), name='post-delete'),
    path('category/', CategoryList.as_view(), name='category'),
    path('category/create/', CategoryCreate.as_view(), name='category-create'),
    path('category/update/<int:pk>', CategoryUpdate.as_view(), name='category-update'),
    path('category/delete/<int:pk>', CategoryDelete.as_view(), name='category-delete'),
    
]
