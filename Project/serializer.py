
from rest_framework import serializers

# 1，定义序列化类 继承serializer类或子类
from rest_framework.validators import UniqueValidator
from Project.models import Projects


#创建自定义校验器
"""
1,name 为需要校验的字段
2, 使用： 添加到字段所属的validators中
3， serializers.ValidationError 返回报错的提示信息
"""
def is_unique_project_name(name):
    if len(name) <= 6:
        raise serializers.ValidationError('项目名称必须大于6')

class ProjectSerializer(serializers.Serializer):
    '''
    #创建序列化器类
    1，序列换器定义的类属性往往与模型类字段一一对应，不一致只能用于校验不能用于序列化输出

    '''

    """
    1.label 相当与verbose_name  help_text 与模型类中的完全一致
    2.需要输出那些字段，那么就在序列化中定义那些字段
    3.read_only 该字段仅用于序列化输出
    4. 定义的默认字段，即用于序列化输出，也用于反序列化输入
    5，write_only 该字段仅用于反序列化输入
    6，如果不需要校验也不需要输出不用定义
    """
    id = serializers.IntegerField(label='ID' ,read_only=True)
    '''
    #判断输入的name是否重复
     1，使用自带的 UniqueValidator 判断  错误显示：message中的提示文字  
    '''
    name = serializers.CharField(label='项目名称', max_length=200, min_length=6, help_text='项目名称提示',validators=
    [UniqueValidator(queryset=Projects.objects.all(),message='项目名不能重复'),is_unique_project_name],error_messages={
        'max_length': "长度不能大于200",
        'min_length' : '长度不能小于6个字节',
    })
    leader = serializers.CharField(label='负责人', max_length=50, help_text='负责人')
    tester = serializers.CharField(label=' 测试人员', max_length=50, help_text='测试人员')
    programer = serializers.CharField(label='开发人员', max_length=200, help_text='开发人员')
    publish_app = serializers.CharField(label='发布应用', max_length=200, help_text='发布应用')
    #allow_null 对应模型类中的null  allow_blank对应模型类中的balank
    desc = serializers.CharField(label='简要描述', help_text='发布应用', allow_blank=True,  allow_null=True)

    #单字段校验
    '''
    校验器的顺序
    1，字节中的数据按照从左到右
    2，自定义的校验器
    3，序列化类里面的校验器（以validate开头_字节名）不需要加入所属的validators中 ,校验成功后必须返回校验值
    '''
    def validate_name(self,value):
        if not  value.endswith('项目'):
            raise serializers.ValidationError('必须是"项目"结尾')
        return value

    #多字段校验
    def validate(self, attrs):
        if 'icon' not in  attrs['leader'] or 'icon' not in attrs['tester']:
            raise serializers.ValidationError('测试和开发人员必须为icon')
        return attrs


    #在序列化期中进行创建，更新
    def create(self, validated_data):
        project = Projects.objects.create(**validated_data)
        return project

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.tester = validated_data['tester']
        instance.programer = validated_data['programer']
        instance.publish_app = validated_data['publish_app']
        instance.desc = validated_data['desc']
        instance.save()
        return instance

#简化序列换器的创建

class ProjectModelSerializer(serializers.ModelSerializer):
    #自定义字段会将自动生成的覆盖掉
    name = serializers.CharField(label='项目名称', max_length=200, help_text='项目名称提示', validators=
    [UniqueValidator(queryset=Projects.objects.all(), message='项目名不能重复'), is_unique_project_name])

    #父表反向指定子表(父表默认不会生成关联字段（从表），可以手动指定，子表名默认 子表模型类名小写_set)
    # Project2s_set = serializers.StringRelatedField(many=True)
    # 指定参考哪一个模型类
    class Meta:
        #指定模型类
        model = Projects
        #指定模型类那些字段来生成序列化期
        #设置需要的字段fields
        fields = "__all__"
        #如果添加一个Projects不存在的字段，必须包裹在fields中
        # fields = ('id','name','leader','tester')
        #设置排除的字段
        # exclude = ('programer','publish_app')
        #设置只需要用于序列换输出
        # read_only_fields = ('tester',)
        # #修改字段设置
        # extra_kwargs = {
        #     'leader': {
        #         'write_only': True,
        #         'error_messages': {
        #             'max_length': "长度不能大于200",
        #             'min_length': '长度不能小于6个字节',
        #         },
        #         'validators' :[UniqueValidator(queryset=Projects.objects.all(),message='项目名不能重复'),
        #                        is_unique_project_name],
        #
        #     }
        #
        #  }

        def validate_name(self, value):
            if not value.endswith('项目'):
                raise serializers.ValidationError('必须是"项目"结尾')
            return value

        # 多字段校验
        def validate(self, attrs):
            if 'icon' not in attrs['leader'] or 'icon' not in attrs['tester']:
                raise serializers.ValidationError('测试和开发人员必须为icon')
            return attrs
