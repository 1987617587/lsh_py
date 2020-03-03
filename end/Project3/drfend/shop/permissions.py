"""
自定义权限
"""
from rest_framework import permissions


class CategoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True


class OrdersPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj, request.user)
        # if obj.user == request.user:
        #     return True
        return obj.user == request.user
