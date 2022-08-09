from django.urls import path
from .views import PostList

app_name = "api"

urlpatterns = [
    path("", PostList.as_view(), name="list"),
]
