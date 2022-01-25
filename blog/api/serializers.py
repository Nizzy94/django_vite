from rest_framework import serializers

from blog.models import Blog, Category


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'slug'


class BlogSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
        lookup_field = 'slug'
