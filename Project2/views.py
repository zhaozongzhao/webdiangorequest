from django.shortcuts import render
from django.http import JsonResponse
from Project2.models import Project2s
from django.db.models import Count,Avg

# Create your views here.

def interfaces(request):

     #分组查询
     # qs = Project2s.objects.all().annotate(h = Count('project_id'))
     qs = Project2s.objects.values('project_id').annotate(Count('project_id'))


     return JsonResponse(data='完成',safe=False)
