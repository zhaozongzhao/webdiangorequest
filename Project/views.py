from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# 函数视图
# 视图函数第一个参数一般默认为request


def index(request):
    '''
     :param requext: # request是HTTprequest对象，白喊前端的所有请求信息
     :return:  必须返回一个HttpReponse对象或者子对象
    '''
    if request.method == 'GET':
       return HttpResponse('<h1>星空<h1>')
    elif request.method == "POST":
        return HttpResponse('<h1>黑夜<h1>')
    else:
        return HttpResponse('<h1>星星<h1>')

#类视图
class Indexview(View):

    def get(self,request):

        # return HttpResponse('<h1>星空<h1>')
        # 从数据库中读取数据
        datas = [
            {'project':'11',
             'leader':'22'},
            {'project': '33',
             'leader': '44'},
        ]
        return  render(request,'test.html',locals())
    def post(self,request):
        return HttpResponse('<h1>黑夜<h1>')

    def delete(self,request):
        return HttpResponse('<h1>星星<h1>')
