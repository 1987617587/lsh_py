from django.template import Library
from ..models import Article, Category, Tag

# 编译过滤器
register = Library()


# 使用装饰器
@register.filter
def date_format(date):
    return "%d-%d-%d" % (date.year, date.month, date.day)


@register.filter
def author_format(author, info):
    return info + ":" + author.upper()


@register.simple_tag
def get_latest_articles(num=3):
    return Article.objects.all().order_by("-create_time")[:num]


@register.simple_tag
def get_latest_dates(num=3):
    return Article.objects.dates("create_time", 'month', "DESC")[:num]

@register.simple_tag
def get_categories():
    return Category.objects.all().order_by("id")[::]



@register.simple_tag
def get_tags():
    return Tag.objects.all().order_by("id")[::]