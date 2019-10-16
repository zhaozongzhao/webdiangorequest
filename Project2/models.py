from django.db import models


# Create your models here.

# 一份项目有多个接口
# 在多的一侧创建外键
# 项目表为父表，接口表为子表
class Project2s(models.Model):
    name = models.CharField(verbose_name='接口名称', max_length=200, unique=True, help_text='接口名称')
    tester = models.CharField(verbose_name=' 测试人员', max_length=50, help_text='测试人员')
    desc = models.TextField(verbose_name='简要描述', help_text='发布应用', blank=True, default='', null=True)
    # 第一个参数为关联模型路径（应用名。模型类）或者模型类
    # 第二个参数设置的是，父表删除之后，该字段的处理方式
    # CASCADE代表子表会被删除 SET_NULL 子表设置为空 PROJECT 父表删除会报错 SET_DEFAULI 设置为空
    project = models.ForeignKey('Project.Projects', on_delete=models.CASCADE, verbose_name='所属项目', help_text='所属项目')

    # 定义子类，用于设置当前数据库模型的元数据信息
    class Meta:
        """
        db_table .设置表名
        verbose_name 会在andmin站点中，显示一个更人性的表名
        """
        db_table = 'ta_interfaces'
        verbose_name = '接口'
        verbose_name_plural = '接口'

    def __str__(self):
        return self.name
