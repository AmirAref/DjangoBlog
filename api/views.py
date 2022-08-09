from rest_framework.generics import ListAPIView
from blog.models import Post
from .serializers import PostSerilizer

# Create your views here.
class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerilizer