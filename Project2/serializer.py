
from rest_framework import serializers
from Project2.models import Project2s
from Project.models import Projects
from Project.serializer import ProjectSerializer
# 1，定义序列化类 继承serializer类或子类
from rest_framework.validators import UniqueValidator


#简化序列换器的创建

class InterfaceModelSerializer(serializers.ModelSerializer):

    """
    1.数据库模型中的外键字段，默认会生成（PrimaryKeyRelatedField）序列化器
    序列化输出的值值外键的ID值


    """
    #数据库模型中的外键字段设置为StringRelatedField，此字段将被序列化为关联对象字符串表达形式（project中的__str__方法）
    # project = serializers.StringRelatedField(label='所属项目')
    #此字段将被序列化为关联字典的指定字段
    # project = serializers.SlugRelatedField(label='所属项目', slug_field='tester',queryset=Projects.objects.all())
    #指定为外键所属项目的序列换器
    project = ProjectSerializer(label='所属项目' ,read_only=True)
    # 指定参考哪一个模型类
    class Meta:
        #指定模型类
        model = Project2s
        #指定模型类那些字段来生成序列化期
        #设置需要的字段fields
        fields = "__all__"
