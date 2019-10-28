from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# 导入排序
from rest_framework.generics import GenericAPIView
from rest_framework import filters
import json
# 导入模型类
from Project.models import Projects, Person
# 导入序列化器
from Project.serializer import ProjectSerializer, ProjectModelSerializer
#导入过滤引擎
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins


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
class Indexview(APIView):

    def get(self, request, pk):
        # return HttpResponse('<h1>星空<h1>')
        # 从数据库中读取数据
        datas = [
            {'project': '11',
             'leader': '22'},
            {'project': '33',
             'leader': '44'},
        ]
        # return render(request, 'test.html', locals())
        return Response(request.data, template_name='test.html')

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


class ProjectsView(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):


    # 指定查询集合（所有的查询数据）
    queryset = Projects.objects.all()
    # 指定序列化器
    serializer_class = ProjectModelSerializer
    # 在视图类中指定过滤引擎（可以指定多个过滤器） OrderingFilter排序过滤器  DjangoFilterBackend(筛选)
    filter_backends = [filters.OrderingFilter,DjangoFilterBackend]
    # 对特定字段进行排序,指定排序的字段
    ordering_fields = ['name', 'leader']
    #对特定的筛选字段
    filterset_fields = ['name', 'leader']

    def get(self, request,*args, **kwargs):

        # project_qs = self.get_queryset()
        # '''
        #  序列化器如果返回多条数据 需要添加：many=True
        # '''
        # project_qs = self.filter_queryset(project_qs)  # 过滤查询集
        #
        # page = self.paginate_queryset(project_qs) #使用paginate_queryset进行分页操作，返回分页之后的查询集
        #
        # if page is not None:
        #     serialier = self.get_serializer(instance=page, many=True)
        #     #使用self.get_paginated_response 返回
        #     return  self.get_paginated_response(serialier.data)
        # serialier = self.get_serializer(instance=project_qs, many=True)
        # return Response(serialier.data)
        return  self.list(request,*args,**kwargs)

    def post(self, request,*args, **kwargs):

        '''
        新增项目
        :param request:  传入的参数
        :return:
        '''

        """
        当视图函数继承APIView之后
        1.请求实例方法，第二个参数request为Request对象，是对Django中HTTPRequest扩展
        """

        # # 反序列化
        # serializer = ProjectSerializer(data=request.data)
        # """
        # #校验前端输入的数据
        # 1，校验输入的数据，调用is_valid()才开始校验前端输入的数据，成功Treu 失败False
        # 2，raise_exception=True 校验失败会抛出异常，成功Treu
        # 3，当调用is_valid 用 serializer.errors 获取错误信息
        # 4. 校验成功的数据 用serializer.validated_data 获取
        # """
        # try:
        #     serializer.is_valid(raise_exception=True)
        # except Exception as e:
        #     return Response(serializer.errors)
        #
        # # 使用序列化器代替创建数据
        # """
        # 1,如果调用序列化期中只给data传参，那么serializer.save()实际调用的是序列化期中的create()
        # """
        # serializer.save()
        #
        # return Response(serializer.data, status=201)
        return self.create(request,*args, **kwargs)


# 需要继承GenericAPIView
class ProjrctView2(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView):
    # 必须指定queryset和serializer_class

    queryset = Projects.objects.all()  # 用于指定需要使用的查询集

    serializer_class = ProjectModelSerializer  # 用于指定用到的序列化器类

    filter_backends = [filters.OrderingFilter] #指定排序过滤引擎



    # GenericAPIView中提供的get_object
    # def get_object(self, pk):
    #     try:
    #         return Projects.objects.get(id=pk)
    #     except Projects.DoesNotExist:
    #         raise Http404

    #如果使用不是pk可以自定义lookup_field，可以修改
    # lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        #
        # project = self.get_object()  # 使用get_object()不需要自定义
        #
        # """
        #  1.通过模型类对象（或者查询集），传给Instance可进行序列化操作
        #  2.通过序列化serializer对象data属性，就可以获取转换之后的字典
        # """
        # serializer = self.get_serializer(instance=project) #使用get_serializer 获取序列化器类
        #
        # return Response(serializer.data, status.HTTP_200_OK)
        return  self.retrieve(request,*args, **kwargs)

    def put(self, request, *args, **kwargs):

        # project = self.get_object()
        # serializer = self.get_serializer(instance=project, data=request.data)
        # try:
        #     serializer.is_valid(raise_exception=True)
        # except Exception as e:
        #     return Response(serializer.errors, safe=True)
        #
        # serializer.save()
        #
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):

        # project = self.get_object()
        # project.delete()
        # return Response(data=None, status=204)
        return self.destroy(request, *args, **kwargs)


# 使用序列化器创建的类
class ProjrctViewserializers(View):
    pass


class ProjrctViewserializers2(View):
    pass
