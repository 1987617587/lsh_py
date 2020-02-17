from django.shortcuts import render, redirect, reverse
from django.template import loader
from django.http import HttpResponse

from .models import Problem, Option


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
def result(request, problemid):
    problem = Problem.objects.get(id=problemid)
    return render(request, 'vote/result.html',{'problem': problem})
