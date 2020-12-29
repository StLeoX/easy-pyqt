# coding=utf-8
"""
    create by pymu on 2020/6/18
    package: .main.py
    程序启动代码
"""

from common.base.launch import EasyQtInit
from example.view.test_activity import TestActivity

if __name__ == '__main__':
    EasyQtInit(TestActivity()).run()
