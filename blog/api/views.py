
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
    print(categories)

    selected_cats = categories.filter(
        blogs__count__gt=4).order_by('?')[:2]

    print('list', list(selected_cats))

    sel_cat_list = list(selected_cats)

    latest = blogs[:4]

    # sel_cat1_blogs = []
    # sel_cat2_blogs = []
    sel_cat1_blogs = sel_cat_list[0].blogs.order_by("-created_at")
    sel_cat2_blogs = sel_cat_list[1].blogs.order_by("-created_at")

    print('selected_cats', selected_cats)
    print('selected_cats0', sel_cat_list[0])
    print('selected_cats1', sel_cat_list[1])
    print('latest:', latest)
    print('before:', {
        'sel_cat1_blogs': sel_cat1_blogs,
        'sel_cat2_blogs': sel_cat2_blogs
    })
    for lat in latest:
        for blog in sel_cat1_blogs:
            if blog.id == lat.id:
                sel_cat1_blogs = sel_cat1_blogs.exclude(id=blog.id)

        for blog in sel_cat2_blogs:
            if blog.id == lat.id:
                sel_cat2_blogs = sel_cat2_blogs.exclude(id=blog.id)

    print('after:', {
        'sel_cat1_blogs': sel_cat1_blogs[:4],
        'sel_cat2_blogs': sel_cat2_blogs[:4]
    })
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
