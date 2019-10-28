from rest_framework.pagination import PageNumberPagination


#自定义分页引擎类
class PageNumberPaginationManul(PageNumberPagination):
    page_query_param = 'p'
    #设置每页显示条数
    page_size = 10
    #设置最大分页数
    max_page_size = 50
    #设置每页显示数量
    page_size_query_param = 's'
