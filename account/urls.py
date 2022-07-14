from django.contrib.auth.views import LoginView
from django.urls import path
from .views import PostList, PostCreate, PostUpdate, PostDelete

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  
    path('', PostList.as_view(), name='home'),   
    path('create', PostCreate.as_view(), name='post-create'),
    path('update/<int:pk>', PostUpdate.as_view(), name='post-update'),
    path('delete/<int:pk>', PostDelete.as_view(), name='post-delete'),
]
