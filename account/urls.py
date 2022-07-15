from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import PostList, PostCreate, PostUpdate, PostDelete

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('', PostList.as_view(), name='home'),   
    path('create', PostCreate.as_view(), name='post-create'),
    path('update/<int:pk>', PostUpdate.as_view(), name='post-update'),
    path('delete/<int:pk>', PostDelete.as_view(), name='post-delete'),
]
