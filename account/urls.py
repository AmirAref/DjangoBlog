from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView
from django.urls import path
from .views import (
    PostList,
    PostCreate,
    PostUpdate,
    PostDelete,
    Profile,
    Login,
    PasswordChange,
    )

app_name = 'account'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),  
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile/', Profile.as_view(), name='profile'),  
    path('', PostList.as_view(), name='home'),   
    path('create', PostCreate.as_view(), name='post-create'),
    path('update/<int:pk>', PostUpdate.as_view(), name='post-update'),
    path('delete/<int:pk>', PostDelete.as_view(), name='post-delete'),
]
