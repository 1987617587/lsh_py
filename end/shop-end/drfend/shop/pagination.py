from rest_framework import pagination

class MyPagination(pagination.PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'num'