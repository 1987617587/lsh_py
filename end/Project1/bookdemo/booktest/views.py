from django.shortcuts import render,reverse,redirect
from .models import Book,Hero
# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse("这里是首页")
    books = Book.objects.all()
    return render(request,'index.html',{'books':books})

def detail(request,b_id):
    book = Book.objects.get(id = b_id)
    book.pub_date = book.pub_date.strftime("%Y-%m-%d")
    return render(request,'detail.html',{'book':book})

def delbook(request,bookid):
    book = Book.objects.get(id = bookid)
    book.delete()
    url = reverse('booktest:index')
    # 使用重定向
    return redirect(to=url)


def addbook(request):
    if request.method == 'GET':
        return render(request,'addbook.html')
    elif request.method == 'POST':
        b = Book()
        b.title =request.POST.get("title")
        print(b.title)
        b.price =request.POST.get("price")
        # h.gender = True
        b.pub_date = request.POST.get("pub_date")

        b.save()
        url = reverse("booktest:index")
        return redirect(to=url)

def delhero(request,heroid):
    hero = Hero.objects.get(id=heroid)
    # 一定要先获取在删除
    bookid = hero.book.id
    hero.delete()
    url = reverse("booktest:detail",args=(bookid,))
    return redirect(to=url)

def addhero(request,bookid):
    print(bookid)
    if request.method == 'GET':
        return render(request, 'addhero.html')
    elif request.method == 'POST':
        h = Hero()
        h.name = request.POST.get("heroname")
        print(h.name)
        h.gender = request.POST.get("sex")
        # h.gender = True
        h.content = request.POST.get("content")
        h.book = Book.objects.get(id=bookid)
        h.save()
        url = reverse("booktest:detail", args=(bookid,))
        return redirect(to=url)


def edithero(request,heroid):
    hero = Hero.objects.get(id = heroid)
    print(hero)
    # 使用get方法进入英雄的编辑页面
    if request.method == 'GET':
        return render(request,"edithero.html",{'hero':hero})
    elif request.method == 'POST':
        hero.name = request.POST.get("heroname")
        hero.gender = request.POST.get("sex")
        hero.content = request.POST.get("content")
        hero.save()
        # 注意数组类型 不加，会报类型错误的
        url = reverse('booktest:detail',args=(hero.book.id,))
        return redirect(to=url)


def editbook(request,bookid):
    book = Book.objects.get(id = bookid)
    print(book)
    print(book.pub_date)
    # book.pub_date = str(book.pub_date)
    book.pub_date = book.pub_date.strftime("%Y-%m-%d")
    print(type(book.pub_date))
    # 使用get方法进入英雄的编辑页面
    if request.method == 'GET':
        return render(request,"editbook.html",{'book':book})
    elif request.method == 'POST':
        book.name = request.POST.get("title")
        book.price = request.POST.get("price")
        book.pub_date = request.POST.get("pub_date")
        book.save()
        # 注意数组类型 不加，会报类型错误的
        url = reverse('booktest:index')
        return redirect(to=url)