from rest_framework import serializers
from blog.models import Post

class PostSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = (
            'created',
            'hits',
            )