
from blog.api.serializers import BlogSerializer, CategorySerializer
from blog.models import Blog, Category
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import random
import json
from django.db.models import Count


@api_view(['GET'])
@permission_classes([AllowAny])
def get_home_posts(request):

    blogs = Blog.objects.order_by("-created_at")

    categories = Category.objects.annotate(Count('blogs'))

    selected_cats = categories.filter(
        blogs__count__gt=4).order_by('?')[:2]

    sel_cat_list = list(selected_cats)

    latest = blogs[:4]

    sel_cat1_blogs = sel_cat_list[0].blogs.order_by("-created_at")
    sel_cat2_blogs = sel_cat_list[1].blogs.order_by("-created_at")

    for lat in latest:
        for blog in sel_cat1_blogs:
            if blog.id == lat.id:
                sel_cat1_blogs = sel_cat1_blogs.exclude(id=blog.id)

        for blog in sel_cat2_blogs:
            if blog.id == lat.id:
                sel_cat2_blogs = sel_cat2_blogs.exclude(id=blog.id)

    latest_serializer = BlogSerializer(latest, many=True)
    sel_cat1_blogs_serializer = BlogSerializer(sel_cat1_blogs[:5], many=True)
    sel_cat2_blogs_serializer = BlogSerializer(sel_cat2_blogs[:5], many=True)

    cats = CategorySerializer(selected_cats, many=True)

    data = json.dumps({
        'latest': latest_serializer.data,
        'cat1_blogs': sel_cat1_blogs_serializer.data,
        'cat2_blogs': sel_cat2_blogs_serializer.data,
        'cats': cats.data
    })

    # return Response(latest_serializer.data)
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_posts(request, category):
    if category == 'all':
        blogs = Blog.objects.order_by("-created_at")

    else:
        blogs = Blog.objects.filter(category__slug=category)

    serializer = BlogSerializer(blogs, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_post_detail(request, post_slug):
    blog = Blog.objects.filter(slug=post_slug).get()

    serializer = BlogSerializer(blog)
    # serializer = BlogSerializer()

    print(repr(serializer))

    return Response(serializer.data)
