from django.contrib import admin
#导入模型类
from Project.models import Projects,Person

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    '''
     定制后台管理站点类

    '''
    # 指定在修改（新增）中需要展示的字段
    fields = ('name','leader','tester','programer','publish_app','desc')

    #指定要列出的字段
    list_display = ['id','name','leader','tester']

class PersonAdmin(admin.ModelAdmin):
    # 指定在修改（新增）中需要展示的字段
    fields = ('first_name','last_name')
    # 指定要列出的字段
    list_display = ['first_name','last_name']


#设置后台管理的模型
#第一个为数据库模型类， 定制后台管理站点类
admin.site.register(Projects,ProjectAdmin)

admin.site.register(Person,PersonAdmin)

#用户名zzz 密码zzz123456