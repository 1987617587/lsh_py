from django.shortcuts import render, redirect, reverse
from django.template import loader
from django.http import HttpResponse

from .models import Problem, Option, User
from .form import LoginForm,RegistForm

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
        # 1.传统 需要自己编写html表单
        # return render(request, 'vote/login.html', )
        # 2. 使用表单类html表单
        lf = LoginForm()
        return render(request, 'vote/login.html',{'lf':lf} )
    elif request.method == "POST":
        lf = LoginForm(request.POST)
        if lf.is_valid():
            username = lf.cleaned_data["username"]
            password = lf.cleaned_data["password"]


            # username = request.POST.get("username")
            # password = request.POST.get("password")
            # 验证登录可以使用django自带的用户认证系统 认证成功返回用户 失败返回 None
            # user = authenticate(username = username,password = password)
            user = User.objects.get(username=username)
            print(user)
            print(user.password)
            # 因为使用表单类用户的密码是未加密状态，不能使用django登录认证系统
            if user.password == password:
            # if user:
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
                # url = reverse("vote:login")
                # return redirect(to=url)
                return render(request, "vote/login.html", {'errors': "用户名或密码错误","lf":lf})

        # return HttpResponse("登录")
        else:
            return HttpResponse("出现未知错误，登录失败")


def regist(request):
    if request.method == "GET":
        # return render(request, 'vote/regist.html')
        # 3.使用模型表单类
        rf = RegistForm()
        return render(request,"vote/regist.html",{"rf":rf})

    elif request.method == "POST":
        rf = RegistForm(request.POST)
        if rf.is_valid():
            print(rf, rf.cleaned_data["username"])

            username = rf.cleaned_data["username"]
            password = rf.cleaned_data["password"]
            repassword = rf.cleaned_data["repassword"]

            # 模型表单自带用户查重，无法注册重复用户名，不需要自己检测
            if password !=repassword:
                # return HttpResponse("密码不一致")
                return render(request, "vote/regist.html", {'errors': "密码不一致","rf":rf})

            else:
                # User.objects.create_user(username=username,password=password)
                rf.save()
                url = reverse("vote:login")
                return redirect(to=url)
        else:
            return render(request, "vote/regist.html", {'errors': "用户名已存在或密码不一致", "rf": rf})


    #     username = request.POST.get("username")
    #     password = request.POST.get("password")
    #     repassword = request.POST.get("repassword")
    #     if User.objects.filter(username = username).count() > 0:
    #         # return HttpResponse("用户名已存在")
    #         return render(request,"vote/regist.html",{'errors':"用户名已存在","rf":rf})
    #     else:
    #         if password !=repassword:
    #             # return HttpResponse("密码不一致")
    #             return render(request, "vote/regist.html", {'errors': "密码不一致","rf":rf})
    #
    #         else:
    #             # User.objects.create_user(username=username,password=password)
    #             rf.save()
    #             url = reverse("vote:login")
    #             return redirect(to=url)
    # # return HttpResponse("注册")
    # else:
    #     return HttpResponse("出现未知错误，注册失败")

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
