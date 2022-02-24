
from rest_framework import serializers
from django.contrib.auth.models import User

from blog.models import Blog, Category, Tag, Comment
from authentication.api.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'slug'


class TagSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'
        lookup_field = 'slug'


class BlogSerializer(serializers.ModelSerializer):
    # def get_authour(self):
    #     return User.objects.get(self.author)

    url = serializers.CharField(source='get_absolute_url', read_only=True)
    author = UserSerializer()

    class Meta:
        model = Blog
        fields = '__all__'
        lookup_field = 'slug'


# class Child2CommentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Comment
#         fields = '__all__'


class ChildCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # children = serializers.ListSerializer(
    #     child=Child2CommentSerializer()
    # )

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    children = serializers.ListSerializer(
        child=ChildCommentSerializer()
    )

    class Meta:
        model = Comment
        fields = '__all__'
        # depth = 2
