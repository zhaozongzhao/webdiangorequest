from django.contrib import admin

# Register your models here.
from Project2.models import Project2s


class Project2sAdmin(admin.ModelAdmin):
    # 指定在修改（新增）中需要展示的字段
    fields = ('name', 'tester','desc','project')
    # 指定要列出的字段
    list_display = ['name', 'tester','desc','project']

admin.site.register(Project2s,Project2sAdmin)