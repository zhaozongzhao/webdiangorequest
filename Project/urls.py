
from django.urls import path
from Project.views import index
from Project import views

#子路由配置信息
# 每一个应用（模块）都会维护一个子路由（当前的应用路由信息）
# urlpatterns为固定名称的列表
# 列表中的一个元素，就代表一条路由
# 从上到下进行匹配
# 如果匹配不上会抛出一个404（默认404页面，状态404）

urlpatterns = [
    path('', index),
    # 如果为类视图,path第二个参数为类视图名
    # path('index',views.Indexview.as_view()),

    #int 为路径参数转化器
    #:左边为转化器，右边为参数别名
    # int,slug,uuid
    path('<int:pk>/',views.Indexview.as_view()),
    path('study',views.studyview.as_view())
]
