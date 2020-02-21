from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
from .forms import *
# 分页和分页器
from django.core.paginator import Page, Paginator


# Create your views here.

def index(request):
    # return HttpResponse("首页")
    ads = Ads.objects.all()
    # 接收前端传来的type
    year, month, category_id = None, None, None
    type_page = request.GET.get("type")
    if type_page == "date":
        year = request.GET.get("year")
        month = request.GET.get("month")
        articles = Article.objects.filter(create_time__year=year, create_time__month=month).order_by("-create_time")
    elif type_page == "category":
        category_id = request.GET.get("category_id")
        try:
            category = Category.objects.get(id=category_id)
            articles = category.article_set.all()
        except:
            return HttpResponse("标签不合法！")
    elif type_page == "tag":
        tag_id = request.GET.get("tag_id")
        try:
            tag = Tag.objects.get(id=tag_id)
            articles = tag.article_set.all()
        except:
            return HttpResponse("标签不合法！")
    else:
        articles = Article.objects.all()
    # locals()可以返回作用域 局部变量
    # print(locals())
    # return render(request, 'index.html',locals())
    # 添加分页

    paginator = Paginator(articles, 2)
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)
    # return render(request, 'index.html',{"ads":ads,"page":page})
    return render(request, 'index.html', locals())


def detail(request, articleid):
    # return HttpResponse("详情")
    if request.method == "GET":
        try:
            article = Article.objects.get(id=articleid)
            cf = CommentForm()
            return render(request, 'single.html', locals())
        except:
            return HttpResponse("查无此书")
    else:
        cf = CommentForm(request.POST)
        if cf.is_valid():
            # 此时cf是一个表单，不是实例
            # cf.article = Article.objects.get(id=articleid)
            # 保存前对commit默认值修改为False  comment就是实例了
            comment = cf.save(commit=False)
            comment.article = Article.objects.get(id=articleid)
            comment.save()

            url = reverse("blogapp:detail", args=(articleid,))
            return redirect(to=url)

        else:
            article = Article.objects.get(id=articleid)
            cf = CommentForm()
            errors = "输入格式有误！"
            return render(request, 'single.html', locals())


def contact(request):
    # return HttpResponse("联系我们")
    return render(request, 'contact.html')


def favicon(request):
    return redirect(to="/static/favicon.ico")
