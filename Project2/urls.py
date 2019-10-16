
from Project2.views import interfaces
from django.contrib import admin
from django.urls import path,include

#全局路由配置信息
# urlpatterns为固定名称的列表
# 列表中的一个元素，就代表一条路由
# 从上到下进行匹配，如果成功，django会导入和调用path函数第二个参数指定的视图获取去子路由中匹配
# 如果匹配不上会抛出一个404（默认404页面，状态404）

urlpatterns = [
    path('', interfaces),


]
