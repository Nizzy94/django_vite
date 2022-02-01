
from blog.api.serializers import BlogSerializer, CategorySerializer, TagSerializer
from blog.models import Blog, Category
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .paginations import BlogListPagination
import math
import json
from django.db.models import Count


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_categories(request):

    # categories = Category.objects.order_by('blogs__count')
    categories = Category.objects.annotate(
        Count('blogs')).order_by('-blogs__count')[:8]

    # print(categories.order_by('-blogs__count'))

    # for cat in categories:
    #     print(cat.blogs.count())

    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)


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


def perform_pagination(request, queryset, page_size, paginator):
    page_size = page_size
    sortBy = request.GET.get('sortBy', 'created_at')
    # filter = request.GET.get('filter', '')
    decending = request.GET.get('decending', 'true')

    if decending == 'true':
        decending = True
    else:
        decending = False

    if decending:
        blogs = queryset.order_by(f'-{sortBy}')
    else:
        blogs = queryset.order_by(f'{sortBy}')

    result = paginator.paginate_queryset(blogs, request)

    return result


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_posts(request, category):
    page_size = request.GET.get('rowsPerPage', 2)

    if category == 'all':
        # blogs = Blog.objects.order_by("-created_at")
        blogs = Blog.objects.all()

    else:
        blogs = Blog.objects.filter(category__slug=category)

    if page_size:
        page_size = page_size
    else:
        page_size = math.ceil(len(blogs)/2)

    paginator = BlogListPagination(page_size, math.ceil(len(blogs)/page_size))

    result = perform_pagination(request, blogs, page_size, paginator)
    print(result)

    # serializer = BlogSerializer(blogs, many=True)
    serializer = BlogSerializer(result, many=True)

    # return Response(serializer.data)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_posts_by_tag(request, tag):

    page_size = request.GET.get('rowsPerPage', 4)

    blogs = Blog.objects.filter(tags__slug=tag).order_by("-created_at")

    paginator = BlogListPagination(page_size, math.ceil(len(blogs)/page_size))

    result = perform_pagination(request, blogs, page_size, paginator)
    print(result)

    serializer = BlogSerializer(result, many=True)

    # return Response(serializer.data)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_releted_posts_by_tag(request, post_slug):

    blog = Blog.objects.filter(slug=post_slug).get()

    tags = blog.tags.all()
    print(tags)
    blogs_set = {}
    tag_names = []
    blogs = []

    if tags.count() > 0:
        for tag in tags:
            tag_q = tag.blogs.all().exclude(id=blog.id)
            if len(blogs) == 0:
                print('0')
                blogs = tag_q
            elif len(blogs) > 0:
                print('>0')
                blogs = blogs.union(tag_q)
            # blogs.union(tag.blogs.all())

    print('blogs count:', blogs.count())
    print('blogs:', blogs.order_by('-created_at'))
    related = blogs.order_by('-created_at')[:8]

    serializer = BlogSerializer(related, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_post_detail(request, post_slug):
    blog = Blog.objects.filter(slug=post_slug).get()
    tags = blog.tags.all()

    serializer = BlogSerializer(blog)
    serializer_tag = TagSerializer(tags, many=True)

    return Response({'blog': serializer.data, 'tags': serializer_tag.data})


@api_view(['GET'])
@permission_classes([AllowAny])
def get_tags(request, post_slug):
    blog = Blog.objects.filter(slug=post_slug).get()
    tags = blog.tags.all()

    serializer = BlogSerializer(tags)

    return Response(serializer.data)
