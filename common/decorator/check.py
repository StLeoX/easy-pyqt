# coding=utf-8
"""
    create by pymu on 2020/10/26
    file: check.py
"""
from functools import wraps
from inspect import signature


def check_v_type(*args, **kwargs):
    """
    检查数据类型, 不能通过时会抛出类型异常
    :param args: 变长参数约定
    :param kwargs: 变长参数约定键值对
    :return: 元
    :raise TypeError 类型异常
    """

    def decorate(func):
        signal_object = signature(func)
        # 检验队列
        type_list = signal_object.bind(*args, **kwargs).arguments

        def check_value(): ...

        @wraps(func)
        def wrapper(*_args, **_kwargs):
            # 方法参数列表
            value_list = signal_object.bind(*_args, **_kwargs).arguments
            for value_instance, value in value_list.items():
                pass
