"""macdiango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


#全局路由配置信息
# urlpatterns为固定名称的列表
# 列表中的一个元素，就代表一条路由
# 从上到下进行匹配，如果成功，django会导入和调用path函数第二个参数指定的视图获取去子路由中匹配
# 如果匹配不上会抛出一个404（默认404页面，状态404）

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('Project.urls')),
]
