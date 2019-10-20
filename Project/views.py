from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
import json
# 导入模型类
from Project.models import Projects, Person
# 导入序列化器
from Project.serializer import ProjectSerializer


# Create your views here.

# 函数视图
# 视图函数第一个参数一般默认为request


def index(request):
    '''
     :param requext: # request是HTTprequest对象，包含前端的所有请求信息
     :return:  必须返回一个HttpReponse对象或者子对象
    '''
    if request.method == 'GET':
        return HttpResponse('<h1>星空1<h1>')
    elif request.method == "POST":
        return HttpResponse('<h1>黑夜<h1>')
    else:
        return HttpResponse('<h1>星星<h1>')


# 类视图
class Indexview(View):

    def get(self, request, pk):
        # return HttpResponse('<h1>星空<h1>')
        # 从数据库中读取数据
        datas = [
            {'project': '11',
             'leader': '22'},
            {'project': '33',
             'leader': '44'},
        ]
        return render(request, 'test.html', locals())

    # def get(self,request,pk):
    #     """
    #
    #     :param request:
    #     :param pk:  路径传参，可以使用PK获取参数
    #     :return:
    #     """
    #     return HttpResponse('<h1>get黑夜<h1>')

    def post(self, request):
        return HttpResponse('<h1>黑夜<h1>')

    def delete(self, request):
        return HttpResponse('<h1>星星<h1>')


# 类视图
class studyview(View):

    def get(self, request):
        """

        :param request:
        :param pk:  路径传参，可以使用PK获取参数
        :return:
        """
        # data={
        #     "name":'小明',
        #     'age':16
        # }
        # # HttpResponse，第一个参数为响应体内容
        #
        # # return HttpResponse(content=data,content_type='application/json',status=201,)
        # return JsonResponse(data=data,content_type='application/json',status=201)

        # 创建数据
        # 方法一
        # 创建模型类对象
        # one_obj = Projects(name='这是一个牛逼的项目4',leader='icon',tester='小明1'
        #                    ,programer='若言',publish_app='厉害的项目',desc='描述')
        # # 保存
        # one_obj.save()

        # # 方法二
        # Projects.objects.create(name='这是一个牛逼的项目5',leader='icon',tester='小明1'
        #                    ,programer='若言',publish_app='厉害的项目',desc='描述')

        # 获取数据
        # 方法一获取所有数据,返回一个QuerySet查询集
        # h = Projects.objects.all()
        # print(h[:1])
        # for i in h:
        #     print(i.name)

        # 1获取特定某个指定的记录
        '''
         1.get返回的是一个模型类对象
         2.get只能查询一条数据，查询结果出现多条或者不存在就会报错
         3，get主要用于主键和唯一值的查询
        '''
        # one_Projecr = Projects.objects.get(id=3)

        # 2读取部分数据 filter,exclude
        """
        filter : 返回满足条件的查询集合
        exclude : 返回不满足条件的查询集合
        """
        # #读取id为1的数据
        # qs = Projects.objects.filter(id=1)
        # #读取ID不为1的数据
        # qs1 = Projects.objects.exclude(id=1)

        # 3模糊查询

        # mh = Projects.objects.filter(leader__contains='icon') #包含icon
        # mh1 = Projects.objects.filter(leader__icontains='con') #忽略查询结果的大小写icon
        # mh2 = Projects.objects.filter(leader__startswith='i') #i开头的
        # mh3 = Projects.objects.filter(leader__istartswith='') # 忽略大小
        # mh4 = Projects.objects.filter(leader__endswith='n') #n结尾的
        # mh5 = Projects.objects.filter(leader__iendswith='n')
        # mh6 = Projects.objects.filter(leader__regex='')  #正则匹配
        # mh7= Projects.objects.filter(leader__iregex='')
        # mh8 = Projects.objects.filter(leader__exact='icon') #精确匹配
        # mh9 = Projects.objects.filter(leader__iexact='icon')
        # mh10 = Projects.objects.filter(leader__in=['icon','宋茜'])#包含

        # 4关联查询
        '''
        格式 外键字段__从表字段名__
        如果是多个表 A表__C表__从表字段名_
        '''
        # qs = Projects.objects.filter(project2s__name__contains='创建项目')

        # 5比较查询
        """
        __gt  大于
        __gte 大于等于
        __lt  小于
        __lte 小于等于
        返回查询集
        """
        # qs = Projects.objects.filter(id__gt=3)
        # 6逻辑查询
        '''
        可以组合& 和| 操作符以及使用括号进行分组来编写任意复杂的Q 对象
        允许组合正常的查询和取反(NOT) 查询 '~'
        '''

        # qs1 =Projects.objects.filter(name='接口自动',leader='宋茜') #且的关系
        # from django.db.models import Q
        # qs1 = Projects.objects.filter(Q(leader='icon')|Q(leader='宋茜')) #或的关系
        # qs2 = Projects.objects.filter(Q(leader='icon')&~Q(tester='魏书')) #and的

        # 7.查询集的操作
        """
        7.1 查询集相当与一个列表，支持列表的大多数就操作（数字索引，正向切片，for循环）
        7.2 查询集是对数据库的一种操作
        7.3 查询及会缓存结果
        7.4 惰性查询
        7.5 查询集支持链式操作
        first() 第一个
        """
        # #获取链式查询的第一个结果
        # qs = Projects.objects.filter(leader__contains='icon').filter(tester__contains='小明1').first()
        # qs = Projects.objects.filter(leader__contains='icon').filter(tester__contains='小明1').last()

        # 更新数据
        """
        1.获取要修改的数据
        2.修改
        3.保存
        """
        # one_project =  Projects.objects.get(id=2)
        # one_project.name = '接口自动化项目'
        # one_project.save()

        # #删除数据
        # """
        # 1.获取要删除的模型对象
        # 2.删除
        # 3.保存
        # """
        # one_project = Projects.objects.get(id=5)
        # one_project.delete()  #调用时自动保存

        # 排序操作
        # '''
        # 默认是升序
        # 降序加'-'
        # 当地一个字段相同看第二个字段
        # '''
        # Projects.objects.filter(id__gt=3).order_by('-name','leader')

        # 聚合查询
        '''
        aggregate()是QuerySet 的一个终止子句，意思是说，它返回一个包含一些键值对的字典。键的名称是聚合值的标识符
        ，值是计算出来的聚合值。键的名称是按照字段和聚合函数的名称自动生成出来的。
        为聚合值指定一个名称 名称 = 集合值标识符()
        
        '''
        # from django.db.models import Max,Avg,F,Q,Min,Sum
        # qs = Projects.objects.all().aggregate(idmax = Max('id'),idmin=Min('id'),idavg = Avg('id'),
        #                                       idsum =Sum('id'))

        # F查询两个字段的值做比较
        """
        Django 提供 F() 来做这样的比较。F() 的实例可以在查询中引用字段，来比较同一个 model 实例中两个不同字段的值。
        Django 支持 F() 对象之间以及 F() 对象和常数之间的加减乘除和取模的操作。
        # """
        # from django.db.models import F
        # qs = Projects.objects.filter(leader=F('tester'))

        return JsonResponse('完成', safe=False)

    def post(self, request):
        """
        1.使用request.post['']获取www-from表单参数
        :param request:
        :return:
        """
        # json 中的数据存放在body，使用requer.body来获取
        import json
        # 将字节转换为字符串
        one_str = request.body.decode('utf-8')
        print(one_str)
        # 将字符串转为字典
        one_dice = json.loads(one_str)
        print(type(one_dice))
        print(one_dice)
        return HttpResponse('<h1>黑夜<h1>')

    def delete(self, request):
        return HttpResponse('<h1>星星<h1>')


class ProjectsView(View):

    def get(self, request):
        # 获取数据库信息
        project_qs = Projects.objects.all()
        # 将模型类是实例化转化为字典（嵌套字典的类表）
        # project_list = []
        # for project in project_qs:
        # one_dict = {
        # 'name': project.name,
        # 'leader': project.leader,
        # 'tester': project.tester,
        # 'programer': project.programer,
        # 'publish_app': project.publish_app,
        # 'desc': project.desc,
        # }
        # project_list.append(one_dict)
        # project_list.append({
        #     'name': project.name,
        #     'leader': project.leader,
        #     'tester': project.tester,
        #     'programer': project.programer,
        #     'publish_app': project.publish_app,
        #     'desc': project.desc,
        #
        # })
        # jsonRespose 第一个参数只能为dict字典，如果返回其他类型，需要safe=False
        # return JsonResponse(data=project_list, safe=False, status=200)

        '''
         序列化器如果返回多条数据 需要添加：many=True
        '''
        serialier = ProjectSerializer(instance=project_qs, many=True)
        return JsonResponse(serialier.data, safe=False)

    def post(self, request):

        '''
        新增项目
        :param request:  传入的参数
        :return:
        '''
        # 获取前端传入的参数，转换为Python中的类型
        # 为了严谨需要做校验，例如是否为json

        # 1.
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')
        # 2.向项目中添加数据
        # new_projiet = Projects.objects.create(name=python_data['name'],leader=python_data['leader'],tester=python_data['tester'],
        #                         property=python_data['property'],publish_app=python_data['publish_app'],
        #                         desc=python_data['desc'])
        # 可简写为

        # 反序列化
        serializer = ProjectSerializer(data=python_data)
        """
        #校验前端输入的数据
        1，校验输入的数据，调用is_valid()才开始校验前端输入的数据，成功Treu 失败False
        2，raise_exception=True 校验失败会抛出异常，成功Treu
        3，当调用is_valid 用 serializer.errors 获取错误信息
        4. 校验成功的数据 用serializer.validated_data 获取
        """
        try:
           serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors,safe=True)
        #
        # project = Projects.objects.create(**serializer.validated_data)
        #使用序列化器代替创建数据
        """
        1,如果调用序列化期中只给data传参，那么serializer.save()实际调用的是序列化期中的create()
        """
        serializer.save()



        # 返回数据 将模型类对象转换为字典
        # one_dict = {
        #     'name': project.name,
        #     'leader': project.leader,
        #     'tester': project.tester,
        #     'programer': project.programer,
        #     'publish_app': project.publish_app,
        #     'desc': project.desc,
        # }
        #
        # return JsonResponse(data=one_dict, safe=False, status=201)
        # serializer = ProjectSerializer(instance=project)
        return JsonResponse(serializer.data)


class ProjrctView2(View):

    def get_object(self,pk):
        try:
            return Projects.objects.get(id=pk)
        except Projects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        # 获取前端传递的Pk值，类型是否为正整数，数据库中是否存在等
        # 获取指定pk的项目

        project =  self.get_object(pk)

        # 项模型对象转为字典
        # one_dict = {
        #     'name': project.name,
        #     'leader': project.leader,
        #     'tester': project.tester,
        #     'programer': project.programer,
        #     'publish_app': project.publish_app,
        #     'desc': project.desc,
        # }
        # return JsonResponse(data=one_dict, safe=False, status=201)
        """
         1.通过模型类对象（或者查询集），传给Instance可进行序列化操作
         2.通过序列化serializer对象data属性，就可以获取转换之后的字典
        """
        serializer = ProjectSerializer(instance=project)

        return JsonResponse(serializer.data)

    def put(self, request, pk):
        # 1，获取前端传入的PK值信息
        # 2, 获取指定的指定的项目
        # project = Projects.objects.get(id=pk)
        project =  self.get_object(pk)

        # 3,获取前端传入的修改信息
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')



        serializer =ProjectSerializer(instance=project,data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors, safe=True)

        serializer.save()

        # 4，更新项目
        #serializer.validated_data 获取验证后的数据
        # project.name = serializer.validated_data['name']
        # project.leader = serializer.validated_data['leader']
        # project.tester = serializer.validated_data['tester']
        # project.programer = serializer.validated_data['programer']
        # project.publish_app = serializer.validated_data['publish_app']
        # project.desc = serializer.validated_data['desc']
        # project.save()

        # 5，项模型类转化为字典
        # one_dict = {
        #     'name': project.name,
        #     'leader': project.leader,
        #     'tester': project.tester,
        #     'programer': project.programer,
        #     'publish_app': project.publish_app,
        #     'desc': project.desc,
        # }
        #
        # return JsonResponse(data=one_dict, safe=False, status=201)
        # serializer = ProjectSerializer(instance=project)
        return JsonResponse(serializer.data)

    def delete(self, request, pk):
        # project = Projects.objects.get(id=pk)

        project = self.get_object(pk)
        project.delete()
        return JsonResponse(data=None, safe=False, status=204)


# 使用序列化器创建的类
class ProjrctViewserializers(View):
    pass


class ProjrctViewserializers2(View):
    pass
