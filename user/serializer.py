from rest_framework import serializers
from django.contrib.auth.models import User


# 简化序列换器的创建

class RegisterSerializer(serializers.ModelSerializer):
    '''
    注册
    '''
    password_confirm = serializers.CharField(label='确认密码',
                                             max_length=20,
                                             min_length=6,
                                             help_text='确认密码',
                                             write_only=True,
                                             error_messages={'min_length': '输入密码不能小于6位', 'max_length': '不能大于20'})
    token = serializers.CharField(label='生成的token', help_text='生成的token', read_only=True)

    class Meta:
        # 指定django.contrib.auth.models中的USER
        model = User
        # 执行序列化和反序列化的字段
        fields = ('id', 'username', 'password', 'email', 'password_confirm', 'token')

        extra_kwargs = {
            'username': {
                'label': '用户名',
                'min_length': 6,
                'max_length': 20,
                'help_text': '用户名',
                'error_messages': {
                    'max_length': "用户名不能大于20位",
                    'min_length': '用户名不能小于6',
                },
            },
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'write_only': 'True',
                'required': 'True', #修改邮件为必填

            },
            'password': {
                'label': '密码',
                'min_length': 6,
                'max_length': 20,
                'help_text': '密码',
                'error_messages': {
                    'max_length': "输入密码不能大于20位",
                    'min_length': '输入密码不能小于6位',
                },

            },
        }

    def validate(self, attrs):
        #判断多个字段
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password != password_confirm: #判断输入密码是否一致
            raise serializers.ValidationError('密码不一致')
        return attrs

    def create(self, validated_data):
        # 删除多余的数据
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user

        # 手动创建token
