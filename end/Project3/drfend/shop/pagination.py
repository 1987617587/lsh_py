from rest_framework import pagination


class MyPagination(pagination.PageNumberPagination):
    """
    重写rest_framework下的pagination模块中的PageNumberPagination类
    """
    # 每页多少数据
    page_size = 3
    # 拼接页数的字符http://127.0.0.1:8000/categories/?p=2
    page_query_param = "p"
    # 该页展示多少数据http://127.0.0.1:8000/categories/?num=5
    page_size_query_param = "num"
