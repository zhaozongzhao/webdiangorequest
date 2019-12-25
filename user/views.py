from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from . import serializer
from django.contrib.auth.models import User

# Create your views here.

class RegisterView(CreateAPIView):
    """
    注册接口
    """
    #指定查询集
    queryset = User.objects.all()
    #指定序列换器
    serializer_class = serializer.RegisterSerializer
