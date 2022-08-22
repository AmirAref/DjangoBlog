from rest_framework import serializers
from blog.models import Post

class PostSerilizer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True, source='author.username')
    category = serializers.StringRelatedField(read_only=True, many=True)
    
    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'description',
            'publish',
            'updated',
            'thumbnail',
            'is_special',
            'status',
            'author',
            'category',
        )