from django.shortcuts import render, redirect, reverse
from django.template import loader
from django.http import HttpResponse

from .models import Problem, Option

from django.views.generic import View,TemplateView,ListView,CreateView,DetailView as DV,DeleteView,UpdateView
# View 类是所有视图响应类的基（父）类
# 基于CBV的形式实现

# class IndexView(View):
#     def get(self, request):
#         return HttpResponse("扩展View")

class IndexView(ListView):
    # 方法二、继承的ListView
    # 指明使用的模板
    template_name = "vote/index.html"
    # 指明返回的结果
    queryset = Problem.objects.all()
    # 指明返回字典的键
    context_object_name = "problems"

    # 方法一、继承的TemplateView
    # template_name = "vote/index.html"
    # def get_context_data(self, **kwargs):
    #     return {"problems":Problem.objects.all()}
# Create your views here.
def index(request):
    problems = Problem.objects.all()
    return render(request, 'vote/index.html', {'problems': problems})


def detail(request, problemid):
    if request.method == 'GET':
        try:
            problem = Problem.objects.get(id=problemid)
            # print(problem.option.all)
            return render(request, 'vote/detail.html', {'problem': problem})
        except EnvironmentError as e:
            print(e)

            return HttpResponse("问题不合法！")
    elif request.method == 'POST':
        try:
            print(request.POST.get("option"))
            option_id = request.POST.get("option")
            option = Option.objects.get(id= option_id)
            print(option)
            option.votenums += 1
            option.save()

            # return HttpResponse("投票成功")
            url = reverse("vote:result",args=(problemid,))
            return redirect(to=url)
        except:

            return HttpResponse("问题不合法！")

        # return render(request, 'polls_votenums.html', {'problem': problem})
#
#
class DetailView(View):
    def get(self,request, problemid):
        try:
            problem = Problem.objects.get(id=problemid)
            # print(problem.option.all)
            return render(request, 'vote/detail.html', {'problem': problem})
        except EnvironmentError as e:
            print(e)

            return HttpResponse("问题不合法！")

    def post(self,request, problemid):
        try:
            print(request.POST.get("option"))
            option_id = request.POST.get("option")
            option = Option.objects.get(id=option_id)
            print(option)
            option.votenums += 1
            option.save()

            # return HttpResponse("投票成功")
            url = reverse("vote:result", args=(problemid,))
            return redirect(to=url)
        except:

            return HttpResponse("问题不合法！")


def result(request, problemid):
    problem = Problem.objects.get(id=problemid)
    return render(request, 'vote/result.html',{'problem': problem})


class Result(View):
    def get(self,request,problemid):
        problem = Problem.objects.get(id=problemid)
        return render(request, 'vote/result.html', {'problem': problem})