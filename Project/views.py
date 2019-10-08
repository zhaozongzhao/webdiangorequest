from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View

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

#类视图
class Indexview(View):

    def get(self,request,pk):

        # return HttpResponse('<h1>星空<h1>')
        # 从数据库中读取数据
        datas = [
            {'project':'11',
             'leader':'22'},
            {'project': '33',
             'leader': '44'},
        ]
        return  render(request,'test.html',locals())

    # def get(self,request,pk):
    #     """
    #
    #     :param request:
    #     :param pk:  路径传参，可以使用PK获取参数
    #     :return:
    #     """
    #     return HttpResponse('<h1>get黑夜<h1>')

    def post(self,request):
        return HttpResponse('<h1>黑夜<h1>')

    def delete(self,request):
        return HttpResponse('<h1>星星<h1>')
#类视图
class studyview(View):

    def get(self,request):
        """

        :param request:
        :param pk:  路径传参，可以使用PK获取参数
        :return:
        """
        data={
            "name":'小明',
            'age':16
        }
        # HttpResponse，第一个参数为响应体内容

        # return HttpResponse(content=data,content_type='application/json',status=201,)
        return JsonResponse(data=data,content_type='application/json',status=201)


    def post(self,request):
        """
        1.使用request.post['']获取www-from表单参数
        :param request:
        :return:
        """
        # json 中的数据存放在body，使用requer.body来获取
        import json
        #将字节转换为字符串
        one_str = request.body.decode('utf-8')
        print(one_str)
        #将字符串转为字典
        one_dice = json.loads(one_str)
        print(type(one_dice))
        print(one_dice)
        return HttpResponse('<h1>黑夜<h1>')

    def delete(self,request):
        return HttpResponse('<h1>星星<h1>')
