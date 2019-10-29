from django.urls import path,include
from Project.views import index
from Project import views
from rest_framework import routers

# 子路由配置信息
# 每一个应用（模块）都会维护一个子路由（当前的应用路由信息）
# urlpatterns为固定名称的列表
# 列表中的一个元素，就代表一条路由
# 从上到下进行匹配
# 如果匹配不上会抛出一个404（默认404页面，状态404）

#创建路由对象
router = routers.SimpleRouter()
#注册路由
#第一个参数prefix为路由前缀，一般添加应用名
#第二个参数为viewset视图集，不要添加.as_view()
router.register('project',views.projectViewset)

urlpatterns = [
    # path('', index),
    # 如果为类视图,path第二个参数为类视图名
    # path('index',views.Indexview.as_view()),

    # int 为路径参数转化器
    #:左边为转化器，右边为参数别名
    # int,slug,uuid
    # path('<int:pk>/',views.Indexview.as_view()),
    # path('study',views.studyview.as_view()),
    # path('', views.ProjectsView.as_view()),
    # # path('project/',views.ProjrctViewserializers.as_view()), #序列换器
    # path('project/<int:pk>/', views.ProjrctView2.as_view()),
    # # path('project1/<int:pk>',views.ProjectSerializer.as_view()), #序列化器
    # path('projectset/', views.projectViewset.as_view({
    #
    #     'get': 'list',
    #     'post': 'create',
    # }),name = 'project_list'),
    # path('projectset/<int:pk>/', views.projectViewset.as_view({
    #
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy',
    # })),
    # path('projectset/names/',views.projectViewset.as_view({
    #     'get': 'names',
    # }),name = 'project_name'),
    # path('projectset/<int:pk>/interface/', views.projectViewset.as_view({
    #     'get': 'interface',
    # }), name='project_interface'),

    #3，将自动生成的路由添加中
    path('',include(router.urls))

]
