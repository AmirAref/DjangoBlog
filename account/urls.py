from django.contrib.auth.views import LoginView
from django.urls import path
from .views import home

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  
    path('', home, name='home'),    
]
