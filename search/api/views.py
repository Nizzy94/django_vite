from elasticsearch_dsl import Q
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from blog.api.serializers import BlogSerializer
from blog.documents import BlogDocument
from rest_framework.response import Response
from blog.api.paginations import BlogListPagination
from blog.api.views import perform_pagination
import math
from django.http import HttpResponse


def global_search(query):

    return Q(
        'multi_match',
        query=query,
        fields=[
            'title',
            'body',
            'tags.name',
            'category.name',
        ], fuzziness='auto')


@api_view(['GET'])
@permission_classes([AllowAny])
def search(request, query):
    page_size = request.GET.get('rowsPerPage', 12)
    # query = query
    q = global_search(query)
    search = BlogDocument.search().query(q)

    num_hits = search.count()
    search = search[:num_hits]
    response = search.to_queryset()
    # response = search.execute()

    paginator = BlogListPagination(
        page_size, math.ceil(num_hits/page_size))

    result = perform_pagination(
        request, response, page_size, paginator)

    serializer = BlogSerializer(result, many=True)

    return paginator.get_paginated_response(serializer.data)


class SearchBlogs(APIView, PageNumberPagination):
    blog_serializer = BlogSerializer
    document = BlogDocument
    permission_classes = [AllowAny]

    def get(self, request, query):
        try:
            q = global_search(query)
            search = self.document.search().query(q)
            response = search.execute()
            print(len(response))
            results = self.paginate_queryset(
                response, request, view=self)

            serializer = self.blog_serializer(results, many=True)

            return self.get_paginated_response(serializer.data)

        except Exception as e:
            # return Response(data={'message': e}, status=500)
            return HttpResponse(e, status=500)
