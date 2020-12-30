# coding=utf-8
"""
    create by pymu
    on 2020/12/30
    at 16:50
"""
import functools


def set_instance_method(cls, func):
    """通过反射对实例化对象添加方法"""

    @functools.wraps(func)
    def dummy(*args, **kwargs):
        func(cls, *args, **kwargs)

    setattr(cls, func.__name__, dummy)
