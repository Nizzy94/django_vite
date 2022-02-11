from elasticsearch_dsl import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from blog.api.serializers import BlogSerializer
from blog.documents import BlogDocument
from rest_framework.response import Response
from blog.api.paginations import BlogListPagination
from blog.api.views import perform_pagination
import math


def global_search(query):
    return Q(
        'multi_match',
        query=query,
        fields=[
            'title',
            'body',
            'tags',
            # 'category'
        ], fuzziness='auto')


@api_view(['GET'])
@permission_classes([AllowAny])
def search(request, query):
    page_size = request.GET.get('rowsPerPage', 12)
    query = query
    q = global_search(query)
    search = BlogDocument.search().query(q)
    # response = search.execute()

    paginator = BlogListPagination(
        page_size, math.ceil(len(search.to_queryset())/page_size))

    result = perform_pagination(
        request, search.to_queryset(), page_size, paginator)

    serializer = BlogSerializer(result, many=True)

    print(search)

    # print all the hits
    for hit in search:
        print(hit.title)

    # return Response(response)
    return paginator.get_paginated_response(serializer.data)
