
import math

from django.conf import settings

from authentication.api.serializers import UserSerializer
from blog.api.serializers import (BlogSerializer, CategorySerializer,
                                  CommentSerializer, SubscriptionSerializer,
                                  TagSerializer)
from blog.models import Blog, Category, Comment
from django.core.mail import EmailMultiAlternatives
from django.db.models import Count, prefetch_related_objects

from django.template.loader import get_template
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .paginations import BlogListPagination


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_categories(request):

    # categories = Category.objects.order_by('blogs__count')
    categories = Category.objects.annotate(
        Count('blogs')).order_by('-blogs__count')[:8]

    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_home_posts(request):

    blogs = Blog.objects.order_by("-created_at")

    categories = Category.objects.annotate(Count('blogs'))

    selected_cats = categories.filter(
        blogs__count__gt=4).order_by('?')[:4]

    sel_cat_list = list(selected_cats)

    latest = blogs[:4]

    sel_cat1_blogs = sel_cat_list[0].blogs.order_by("-created_at")
    sel_cat2_blogs = sel_cat_list[1].blogs.order_by("-created_at")
    sel_cat3_blogs = sel_cat_list[2].blogs.order_by("-created_at")
    sel_cat4_blogs = sel_cat_list[3].blogs.order_by("-created_at")
    # sel_cat1_blogs, sel_cat2_blogs, sel_cat3_blogs, sel_cat4_blogs = sel_cat_list.blogs.order_by(
    #     "-created_at")

    for lat in latest:
        for blog in sel_cat1_blogs:
            if blog.id == lat.id:
                sel_cat1_blogs = sel_cat1_blogs.exclude(id=blog.id)

        for blog in sel_cat2_blogs:
            if blog.id == lat.id:
                sel_cat2_blogs = sel_cat2_blogs.exclude(id=blog.id)

        for blog in sel_cat3_blogs:
            if blog.id == lat.id:
                sel_cat3_blogs = sel_cat3_blogs.exclude(id=blog.id)

        for blog in sel_cat4_blogs:
            if blog.id == lat.id:
                sel_cat4_blogs = sel_cat4_blogs.exclude(id=blog.id)

    latest_serializer = BlogSerializer(latest, many=True)
    sel_cat1_blogs_serializer = BlogSerializer(sel_cat1_blogs[:5], many=True)
    sel_cat2_blogs_serializer = BlogSerializer(sel_cat2_blogs[:5], many=True)
    sel_cat3_blogs_serializer = BlogSerializer(sel_cat3_blogs[:5], many=True)
    sel_cat4_blogs_serializer = BlogSerializer(sel_cat4_blogs[:5], many=True)

    cats = CategorySerializer(selected_cats, many=True)

    data = {
        'latest': latest_serializer.data,
        'news_section': [
            {'cat': cats.data[0], 'blogs': sel_cat1_blogs_serializer.data},
            {'cat': cats.data[1], 'blogs': sel_cat2_blogs_serializer.data},
            {'cat': cats.data[2], 'blogs': sel_cat3_blogs_serializer.data},
            {'cat': cats.data[3], 'blogs': sel_cat4_blogs_serializer.data},
        ],
        'cats': cats.data
    }

    # return Response(home_posts_serializer.data)
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
    page_size = request.GET.get('rowsPerPage', 12)

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

    # serializer = BlogSerializer(blogs, many=True)
    serializer = BlogSerializer(result, many=True)

    # return Response(serializer.data)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_posts_by_tag(request, tag):

    page_size = request.GET.get('rowsPerPage', 12)

    blogs = Blog.objects.filter(tags__slug=tag).order_by("-created_at")

    paginator = BlogListPagination(page_size, math.ceil(len(blogs)/page_size))

    result = perform_pagination(request, blogs, page_size, paginator)

    serializer = BlogSerializer(result, many=True)

    # return Response(serializer.data)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_releted_posts_by_tag(request, post_slug):

    blog = Blog.objects.filter(slug=post_slug).get()

    tags = blog.tags.all()

    blogs_set = {}
    tag_names = []
    blogs = []

    if tags.count() > 0:
        for tag in tags:
            tag_q = tag.blogs.all().exclude(id=blog.id)
            if len(blogs) == 0:

                blogs = tag_q
            elif len(blogs) > 0:

                blogs = blogs.union(tag_q)
            # blogs.union(tag.blogs.all())

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


@api_view(['GET'])
@permission_classes([AllowAny])
def get_comments(request, post_id):
    blog = Blog.objects.get(id=post_id)

    parent_comments = blog.comments.parent()

    serializer = CommentSerializer(parent_comments, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_comment(request):

    data = request.data

    serializer = CommentSerializer(
        data=request.data, context={'request': request})

    if data['id']:
        comment = Comment.objects.get(id=data['id'])

        serializer = CommentSerializer(comment,
                                       data=request.data, context={'request': request})

    if serializer.is_valid(raise_exception=True):

        comment = serializer.save(user=request.user)

        com_serializer = CommentSerializer(comment)

        return Response(com_serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def delete_comment(request):

    data = request.data

    if data['id']:
        comment = Comment.objects.get(id=data['id'])

        if comment:
            comment.delete()
            # comments = Comment.objects.order_by("-created_at")
            # serializer = CommentSerializer(comments, many=True)
            return Response({'message': 'Comment Deleted.'})
            # return Response(serializer.data)

    return Response({'message': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([AllowAny])
def subscribe(request):
    data = request.data
    print(data)

    serializer = SubscriptionSerializer(data=data)

    plaintext_template = get_template('blog/emails/subscription.txt')
    html_template = get_template('blog/emails/subscription.html')
    subject, from_email, to = 'Subscription to newsletter', 'from@example.com', data['email']

    d = {
        'first_name': data['first_name'],
        'title': subject,
        'from': from_email,
        'to': to,
        'site_name': settings.SITE_NAME,
        'site_origin': data['url'],
    }

    if serializer.is_valid(raise_exception=True):
        # print(serializer.validated_data)
        serializer.save()

        text_content = plaintext_template.render(d)
        html_content = html_template.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return Response({'message': 'You have susbscribed for our news letter.'})
