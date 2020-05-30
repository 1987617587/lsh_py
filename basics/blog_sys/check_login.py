"""
# author Liu shi hao
# date: 2019/12/11 9:29
# file_name: check_login

"""
from functools import wraps




def check_login(func):
    @wraps(func)
    def wrapper(cls):
        from .UI import UI
        if UI.login_num is not None:
            func(cls)
        else:
            print("*" * 12 + "您还未登录，请先登录！" + "*" * 12)

    return wrapper


def stu_num_repeat(stu_num: int):
    from student_sys import class_manager
    query = class_manager.query_by_stu_num(stu_num)
    if len(query) == 0:
        return True
    return False
