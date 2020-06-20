"""
可以自定义权限
"""
from rest_framework import permissions

class CategorysPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

class OrdersPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # print(obj,"++", request.user)
        # print(obj.user == request.user)
        return obj.user == request.user