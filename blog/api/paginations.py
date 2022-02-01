from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param

import math


class BlogListPagination(PageNumberPagination):
    def __init__(self, page_size, max_page_size) -> None:
        super().__init__()
        self.page_size = page_size
        self.max_page_size = max_page_size
        # self.last_page_strings = ('last',)

    def get_paginated_response(self, data):

        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),

            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'last': self.get_last_link(),
            'results': data,
        })

    def get_last_link(self):
        if not self.page.has_next():
            return None
        url = self.request.build_absolute_uri()
        page_number = self.page.paginator.num_pages
        return replace_query_param(url, self.page_query_param, page_number)
