# coding=utf-8
"""
    create by pymu on 2020/6/18
    package: .main.py
"""

from common.base.eq_init import EasyQtInit
from example.test_activity import TestActivity

if __name__ == '__main__':
    app = EasyQtInit(TestActivity())
    app.run()
