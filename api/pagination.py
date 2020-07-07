from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination


# 基础分页器
class MyPageNumberPagination(PageNumberPagination):
    # 默认指定每页分页的数量
    page_size = 4
    # 可以通过此参数指定分页最大数量
    max_page_size = 5
    # 自定义前端每页分页数量的 key
    page_size_query_param = "page_size"
    # 获取第几页的对象
    page_query_param = "page"


# 偏移分页器
class MyLimitPagination(LimitOffsetPagination):
    # 默认获取的每页数量
    default_limit = 3
    # 自定义前端每页数量的key
    limit_query_param = "limit"
    # 前端指定偏移的数量的key
    offset_query_param = "offset"
    # 每页获取的最大数量
    max_limit = 5
