from django.contrib.auth.views import LoginView
from django.urls import path
from .views import PostList

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  
    path('', PostList.as_view(), name='home'),    
]
