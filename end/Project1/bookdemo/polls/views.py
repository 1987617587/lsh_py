from django.shortcuts import render, redirect, reverse
from django.template import loader
from .models import Problem, Option
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


# 3.在views.py中编写视图函数
def index(request):
    problems = Problem.objects.all()
    return render(request, 'polls_index.html', {'problems': problems})


def detail(request, problemid):
    problem = Problem.objects.get(id=problemid)
    if request.method == 'GET':
        print("get")
        return render(request, 'polls_detail.html', {'problem': problem})
    elif request.method == 'POST':
        print("post")
        print(request.POST.get("p"))
        if request.POST.get("p") == "1":
            print("我选第一项")
            print(problem.option1_votes, "加一")
            problem.option1_votes += 1
            print(problem.option1_votes)
        if request.POST.get("p") == "2":
            print("我选第二项")
            print(problem.option2_votes, "加一")
            problem.option2_votes += 1
            print(problem.option2_votes)
        if request.POST.get("p") == "3":
            print("我选第三项")
            print(problem.option3_votes, "加一")
            problem.option3_votes += 1
            print(problem.option3_votes)
        if request.POST.get("p") == "4":
            print("我选第四项")
            print(problem.option4_votes, "加一")
            problem.option4_votes += 1
            print(problem.option4_votes)
        problem.save()


        return render(request, 'polls_votenums.html', {'problem': problem})


def votenums(request):
    url = reverse("polls:index")
    return redirect(to=url)

def vote(request, problemid):
    print(problemid)
    if request.method == 'GET':
        print("get")
        return render(request, 'polls_vote.html')
    elif request.method == 'POST':
        print("post")

        o = Option()
        o.option1 = request.POST.get("option1")
        o.option2 = request.POST.get("option2")
        o.option3 = request.POST.get("option3")
        o.option4 = request.POST.get("option4")
        if o.option1:
            o = 1
        if o.option2:
            o = 2
        if o.option3:
            o = 3
        if o.option4:
            o = 4
        print(o)
        o.problem = Problem.objects.get(id=problemid)
        o.save()
        url = reverse("polls:votenums ", args=(problemid,))
        return redirect(to=url)
