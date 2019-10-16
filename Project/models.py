from django.db import models


# Create your models here.
#
# 1.每一个应用下的数据库模型类，需要在当前应用下的文件中定义
# 2. 一个数据库模型相当与一个数据表
# 3. 一个类属性相当与数据表中的一个字段
# 4.默认会创建一个会自动递增的ID主键
# 5.一个数据库的模型类必须继承model或者model中的子类
# 6. 默认创建的数据库名为，应用名小写_数据库模型类名小写
class Person(models.Model):
    '''
     继承models中的基类
     创建Person 类
    '''
    id = models.AutoField(primary_key=True)  # primary_key为True 代表递增 ,本行默认创建可略
    first_name = models.CharField(max_length=30)  #
    last_name = models.CharField(max_length=30)

    class Meta:
       db_table = 'ta_person'
       verbose_name = '项目'
       verbose_name_plural = '项目'


class Projects(models.Model):
    """
     verbose_name 别名用于设置更人性化的字段名
     max_length 字段最大长度
     unique 用于设置当前字段是否唯一 ， 默认False
     help_text 设置api文档中的中文名称
     blank  设置前端用户可以不传  default 默认值
     null 设置数据库中字段允许为空
        # models.IntegerField(choices=[])) 限定传入信息为choices中的内容

    """
    name = models.CharField(verbose_name='项目名称', max_length=200, unique=True, help_text='项目名称提示')
    leader = models.CharField(verbose_name='负责人', max_length=50, help_text='负责人')
    tester = models.CharField(verbose_name=' 测试人员', max_length=50, help_text='测试人员')
    programer = models.CharField(verbose_name='开发人员', max_length=200, help_text='开发人员')
    publish_app = models.CharField(verbose_name='发布应用', max_length=200, help_text='发布应用')
    desc = models.TextField(verbose_name='简要描述', help_text='发布应用', blank=True, default='', null=True)

    # 定义子类，用于设置当前数据库模型的元数据信息
    class Meta:
        """
        db_table .设置表名
        verbose_name 会在andmin站点中，显示一个更人性的表名
        """
        db_table = 'ta_projects'
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return  self.name