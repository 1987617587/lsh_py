from django.contrib import admin

# Register your models here.

from .models import Problem,Option,User
from django.contrib import admin
from django.contrib.admin import ModelAdmin

class OptionInline(admin.StackedInline):
    model = Option
    extra = 1

class OptionAdmin(ModelAdmin):
    list_display = ("option","votenums")

class ProblemAdmin(ModelAdmin):
    list_display = ("title","source")
    inlines = [OptionInline]

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(User)
