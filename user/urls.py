#系统模块
from django.urls import path, include

#第三方模块
from rest_framework_jwt.views import obtain_jwt_token

#自定义模块
from . import views

urlpatterns = [

    path('login/', obtain_jwt_token),
    path('register/',views.RegisterView.as_view())
]
