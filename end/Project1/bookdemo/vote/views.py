from django.shortcuts import render, redirect, reverse
from django.template import loader
from django.http import HttpResponse

from .models import Problem, Option, User

from django.views.generic import View, TemplateView, ListView, CreateView, DetailView as DV, DeleteView, UpdateView

from django.contrib.auth import login as lin,authenticate,logout as lout
# View 类是所有视图响应类的基（父）类
# 基于CBV的形式实现

# class IndexView(View):
#     def get(self, request):
#         return HttpResponse("扩展View")


def login(request):
    # return HttpResponse("登录")
    if request.method == "GET":
        return render(request, 'vote/login.html', )
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 验证登录可以使用django自带的用户认证系统 认证成功返回用户 失败返回 None
        user = authenticate(username = username,password = password)
        print(user)
        if user:
            # 认证成功 生成cookie
            lin(request, user)

            # 检验以下 来（登录）之前有没有准备进入详情页
            next_url = request.GET.get("next")
            if next_url:
                url = next_url
            else:
                url = reverse("vote:index")
            return redirect(to=url)
        else:
            url = reverse("vote:login")
            return redirect(to=url)
    # return HttpResponse("登录")


def regist(request):
    if request.method == "GET":
        return render(request,'vote/regist.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        if User.objects.filter(username = username).count() > 0:
            return HttpResponse("用户名已存在")
        else:
            if password !=repassword:
                return HttpResponse("密码不一致")
            else:
                User.objects.create_user(username=username,password=password)
                url = reverse("vote:login")
                return redirect(to=url)
    # return HttpResponse("注册")


def loginout(request):
    # 删除 cookie

    lout(request)
    url = reverse("vote:index")

    return redirect(to=url)
    # return HttpResponse("退出")


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
        print("当前用户",request.user.username)
        if request.user and request.user.username != "":
            # 已经登录
            print(request.user.problems)
            print(type(request.user.problems))
            try:
                problem = Problem.objects.get(id=problemid)
                # print(problem.option.all)
                if problem in request.user.problems.all():
                    print("已经投过票了")
                    url = reverse("vote:result",args=(problemid))
                    return redirect(to=url)
                else:

                    return render(request, 'vote/detail.html', {'problem': problem})
            except EnvironmentError as e:
                print(e)

                return HttpResponse("问题不合法！")
        else:
            # 登录之后 跳转之前点击过的详情页
            url = reverse("vote:login")+"?next=/vote/detail/"+problemid+"/"
            return redirect(to=url)
    elif request.method == 'POST':
        try:
            print(request.POST.get("option"))
            option_id = request.POST.get("option")
            option = Option.objects.get(id=option_id)
            print(option)
            option.votenums += 1
            option.save()
            # 关联用户和问题
            request.user.problems.add(Problem.objects.get(id=problemid))

            # return HttpResponse("投票成功")
            url = reverse("vote:result", args=(problemid,))
            return redirect(to=url)
        except:

            return HttpResponse("问题不合法！")

        # return render(request, 'polls_votenums.html', {'problem': problem})


#
#
class DetailView(View):
    def get(self, request, problemid):
        try:
            problem = Problem.objects.get(id=problemid)
            # print(problem.option.all)
            return render(request, 'vote/detail.html', {'problem': problem})
        except EnvironmentError as e:
            print(e)

            return HttpResponse("问题不合法！")

    def post(self, request, problemid):
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
    return render(request, 'vote/result.html', {'problem': problem})


class Result(View):
    def get(self, request, problemid):
        problem = Problem.objects.get(id=problemid)
        return render(request, 'vote/result.html', {'problem': problem})
